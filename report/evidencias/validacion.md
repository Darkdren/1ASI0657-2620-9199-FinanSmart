# Evidencia de validación — Organización FinanZen

Fecha: **10 de octubre de 2026**, zona horaria America/Lima.
Entorno local: Windows y Python 3.11.9, con las versiones fijadas en
[back/requirements.txt](../../back/requirements.txt).

## Suite del backend

Comando ejecutado dentro de `back`:

```powershell
python -m pytest -q -p no:cacheprovider
```

Resultado observado:

```text
....                                                                     [100%]
4 passed in 0.89s
```

Las pruebas validan registro idempotente/conflicto, resumen y filtrado por
usuario, frontend configurable y API independiente del frontend.
Utilizan bases temporales.

## Integración y documentación

Comprobación reproducible desde la raíz:

```powershell
python scripts/verificar.py
```

El script comprueba las cinco carpetas, enlaces internos, el hash del PDF
original, entrega de HTML/CSS/JavaScript desde `front/`, Swagger, OpenAPI,
registro, consulta y cálculo del resumen con una base temporal.

Resultado observado:

```text
Documentation: 92 relative links OK; original PDF checksum OK.
Integration: front assets, health, Swagger, OpenAPI, registration, listing and monthly summary OK.
FinanZen verification completed.
```

## Contrato API

[openapi.json](openapi.json) se exportó desde `create_app().openapi()` después
de adaptar la ruta del frontend. No se redactaron endpoints futuros como si
existieran. El contrato también está disponible en `/openapi.json` al ejecutar
el backend.

## Fuente documental

El PDF incluido conserva sus 109 páginas y el siguiente SHA-256:

```text
b81f72f9f9c03d0c70d0dcd8934043ee67e3286bf2df98885a912e1040bbdc58
```

La [transcripción](../fuentes/transcripcion_pdf.md) cubre todas sus páginas.
Se conservaron las figuras de investigación, arquitectura y las capturas
históricas del PDF. La página 66 no aporta diagrama de datos: el esquema SQLite
actual se documentó aparte a partir de `repository.py`.

## Alcance de la evidencia

Las comprobaciones son locales y no demuestran despliegue cloud, autenticación
real, rendimiento con 50 usuarios, auditoría, IoT ni proyecciones.
El [workflow de CI](../../.github/workflows/validacion.yml) permite repetir la
suite y el script; sus resultados remotos deben consultarse en GitHub Actions.
Las capturas de `platform` y Postman son evidencia histórica del PDF.
