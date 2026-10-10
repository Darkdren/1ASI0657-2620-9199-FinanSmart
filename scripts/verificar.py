"""Verify the five components, relative documentation links and web/API integration."""

import gc
import hashlib
import os
from pathlib import Path
import re
import sys
from tempfile import TemporaryDirectory
from urllib.parse import unquote, urlsplit
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
COMPONENTS = ("back", "report", "landing", "front", "mobile")
PDF_SHA256 = "b81f72f9f9c03d0c70d0dcd8934043ee67e3286bf2df98885a912e1040bbdc58"


def verify_documentation() -> int:
    for component in COMPONENTS:
        assert (ROOT / component / "README.md").is_file(), component
    checked = 0
    for document in sorted(ROOT.rglob("*.md")):
        relative = document.relative_to(ROOT)
        if any(part in {".git", ".venv", "venv", "node_modules", "entregables"} for part in relative.parts):
            continue
        content = document.read_text(encoding="utf-8-sig")
        for label, target in re.findall(r"!?\[([^\]]+)\]\(([^\s)]+)\)", content):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (document.parent / unquote(parsed.path)).resolve()
            assert destination.is_relative_to(ROOT), (relative, label, target)
            assert destination.exists(), (relative, label, target)
            checked += 1
    pdf = ROOT / "report/fuentes/TF_1ASI0657_202610_NRC_7.pdf"
    assert hashlib.sha256(pdf.read_bytes()).hexdigest() == PDF_SHA256
    print(f"Documentation: {checked} relative links OK; original PDF checksum OK.")
    return checked


def verify_integration() -> None:
    sys.path.insert(0, str(ROOT / "back"))
    from fastapi.testclient import TestClient
    from app.main import create_app

    with TemporaryDirectory(prefix="finanzen-check-") as temporary:
        # Clear only the optional frontend override so the real sibling path is checked.
        with patch.dict(os.environ):
            os.environ.pop("FINANZEN_FRONTEND_PATH", None)
            application = create_app(str(Path(temporary) / "integration.db"))
        try:
            with TestClient(application) as client:
                for route, filename in (("/", "index.html"), ("/styles.css", "styles.css"), ("/app.js", "app.js")):
                    response = client.get(route)
                    assert response.status_code == 200, (route, response.status_code)
                    assert response.content == (ROOT / "front" / filename).read_bytes(), route
                assert client.get("/health").json()["status"] == "ok"
                assert client.get("/docs").status_code == 200
                contract = client.get("/openapi.json")
                assert contract.status_code == 200
                assert "/api/v1/transactions" in contract.json()["paths"]
                payload = {
                    "account_id": "cash-account",
                    "type": "income",
                    "amount": "1500.00",
                    "currency": "PEN",
                    "category": "salary",
                    "occurred_at": "2026-10-01T10:00:00Z",
                }
                created = client.post(
                    "/api/v1/transactions", json=payload,
                    headers={"X-User-Id": "integration-user", "Idempotency-Key": "integration-0001"},
                )
                assert created.status_code == 201
                headers = {"X-User-Id": "integration-user"}
                listed = client.get("/api/v1/transactions", headers=headers)
                assert listed.status_code == 200
                assert len(listed.json()) == 1
                summary = client.get("/api/v1/summary?month=2026-10&currency=PEN", headers=headers)
                assert summary.status_code == 200
                assert summary.json()["balance"] == "1500.00"
        finally:
            # sqlite context managers commit/rollback but do not close connections.
            # Collect those short-lived connections before Windows removes the temp DB.
            gc.collect()
    print("Integration: front assets, health, Swagger, OpenAPI, registration, listing and monthly summary OK.")


if __name__ == "__main__":
    verify_documentation()
    verify_integration()
    print("FinanZen verification completed.")
