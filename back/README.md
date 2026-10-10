# FinanZen — Back

Primer incremento de **Financial Records Service**: API REST para registrar
ingresos y gastos, consultar movimientos y obtener un resumen mensual por usuario.

## Estructura

```text
back/
├── app/
│   ├── __init__.py
│   ├── main.py          FastAPI, endpoints y entrega opcional de front/
│   ├── models.py        Contratos y validación con Pydantic
│   └── repository.py    Persistencia SQLite e idempotencia
├── data/                Base de datos generada al arrancar
├── tests/test_api.py
├── requirements.txt
└── README.md
```

## Ejecutar

Requiere Python 3.10 o superior. Desde la raíz del repositorio:

```powershell
cd back
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

En Linux/macOS, los ejecutables del entorno están en `.venv/bin/python`.

- Interfaz web: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs
- Contrato OpenAPI: http://127.0.0.1:8000/openapi.json
- Estado del servicio: http://127.0.0.1:8000/health

El backend busca `../front` automáticamente. La API también funciona sin esa
carpeta. Si se añade el frontend después del arranque, reiniciar el servidor.
SQLite y su esquema se crean al arrancar; no se versionan datos de ejecución.

## Configuración opcional

```powershell
$env:FINANZEN_FRONTEND_PATH = 'C:\ruta\a\front'
$env:FINANZEN_DB_PATH = 'C:\ruta\a\financial_records.db'
```

Sin estas variables, la base es `data/financial_records.db`, relativa al
directorio de ejecución. Ejecutar los comandos dentro de `back`.

## Endpoints

| Método | Ruta | Función |
| --- | --- | --- |
| GET | `/health` | Estado operativo |
| POST | `/api/v1/transactions` | Registrar ingreso o gasto |
| GET | `/api/v1/transactions` | Movimientos del usuario |
| GET | `/api/v1/summary?month=2026-10&currency=PEN` | Resumen mensual |

Los endpoints financieros requieren `X-User-Id`. El POST también requiere
`Idempotency-Key`, de 8 a 120 caracteres. Un registro nuevo devuelve HTTP 201;
repetir la misma clave y cuerpo devuelve el registro existente con HTTP 200;
reutilizar la clave con otro cuerpo devuelve HTTP 409.

`X-User-Id` simula identidad y no autentica al usuario. No están implementados
OAuth, límites de presupuesto, alertas, IA ni integración IoT. El resumen
mensual constituye soporte parcial de PF-02, sin completar US10, US11 o US12.

## Ejemplo en PowerShell

```powershell
$headers = @{
    'X-User-Id' = 'demo-user'
    'Idempotency-Key' = 'demo-income-0001'
}
$body = @{
    account_id = 'cash-account'
    type = 'income'
    amount = 1500.00
    currency = 'PEN'
    category = 'salary'
    occurred_at = '2026-10-01T10:00:00Z'
} | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:8000/api/v1/transactions' -Headers $headers -ContentType 'application/json' -Body $body
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/api/v1/summary?month=2026-10' -Headers @{ 'X-User-Id' = 'demo-user' }
```

## Pruebas

Dentro de `back`:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

La suite usa bases temporales y verifica idempotencia, conflictos, cálculo del
resumen, aislamiento por identificador, entrega del frontend configurado y
ejecución sin frontend. El registro de validación está en
[report/evidencias/validacion.md](../report/evidencias/validacion.md).
