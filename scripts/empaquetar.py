"""Create one ZIP per component and one complete FinanZen ZIP."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "entregables"
COMPONENTS = ("back", "report", "landing", "front", "mobile")
EXCLUDED = {
    ".git", "__pycache__", ".pytest_cache", ".venv", "venv", "node_modules",
    "dist", "build", ".dart_tool", ".gradle", "entregables", ".idea", ".vscode",
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".db", ".sqlite", ".sqlite3", ".apk", ".aab"}


def files_in(folder: Path):
    for source in sorted(folder.rglob("*")):
        relative = source.relative_to(ROOT)
        if not source.is_file() or any(part in EXCLUDED for part in relative.parts):
            continue
        if source.suffix in EXCLUDED_SUFFIXES or source.name.endswith(("-wal", "-shm", "-journal")):
            continue
        if source.name.startswith(".env") and source.name != ".env.example":
            continue
        if source.name == ".coverage":
            continue
        yield source


def create_zip(filename: str, sources: list[Path], prefix: str = "") -> None:
    output = OUTPUT / filename
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for source in sources:
            name = prefix + source.relative_to(ROOT).as_posix()
            archive.write(source, name)
    with ZipFile(output) as archive:
        assert archive.testzip() is None, filename
    print(f"{output.name}: {len(sources)} files, {output.stat().st_size} bytes")


if __name__ == "__main__":
    OUTPUT.mkdir(exist_ok=True)
    for component in COMPONENTS:
        create_zip(f"FinanZen-{component}.zip", list(files_in(ROOT / component)))
    create_zip("FinanZen-Completo.zip", list(files_in(ROOT)), "FinanZen/")
