# FinanZen

Repositorio contenedor del trabajo final de **Fundamentos de Arquitectura de
Software**, Universidad Peruana de Ciencias Aplicadas. El producto se llama
**FinanZen**; se conserva el nombre existente del repositorio en GitHub.

## Componentes

| Carpeta | Proyecto | Estado |
| --- | --- | --- |
| [back](back/README.md) | API de registros financieros con FastAPI y SQLite | Primer incremento funcional |
| [report](report/README.md) | Informe actualizado, PDF fuente, diagramas y evidencias | Actualizado con el PDF de 109 páginas |
| [landing](landing/README.md) | Presentación pública del producto y equipo | Carpeta preparada; proyecto pendiente |
| [front](front/README.md) | Panel web en HTML, CSS y JavaScript | Funcional y conectado al backend |
| [mobile](mobile/README.md) | Aplicación móvil | Carpeta preparada; proyecto pendiente |

```text
1ASI0657-2620-9199-FinanSmart/
├── back/
├── report/
├── landing/
├── front/
├── mobile/
├── scripts/                 Comprobación de integración y empaquetado
└── .github/workflows/       Validación del backend y documentación
```

Los cinco componentes se gestionan como carpetas de un mismo repositorio Git.
Cada componente tiene su README; no contiene repositorios Git anidados.

## Ejecutar el MVP

Requiere Python 3.10 o superior. Desde la raíz:

```powershell
cd back
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

- Panel web: http://127.0.0.1:8000
- Documentación API: http://127.0.0.1:8000/docs
- Estado: http://127.0.0.1:8000/health

El backend encuentra `front/` automáticamente. La base SQLite se genera al
arrancar. Las variables opcionales se describen en [back/README.md](back/README.md).

## Datos académicos

Datos tomados de la portada del PDF proporcionado:

| Campo | Detalle |
| --- | --- |
| Universidad | Universidad Peruana de Ciencias Aplicadas |
| Carrera | Ingeniería de Software |
| Curso | 1ASI0657 — Fundamentos de Arquitectura de Software |
| Periodo | 202620 |
| NRC | 9199 |
| Profesor | Daniel Enrique Mori Yzaguirre |
| Producto | FinanZen |

| Integrante | Código |
| --- | --- |
| Oblitas Alcalde Rodrigo | U20221G185 |
| Revilla Quispe Renzo Zamir | U201717085 |
| Aguirre Eneque Joan Elias | U202315649 |

## Informe y estado de implementación

El [informe](report/README.md) incorpora los capítulos I–V del PDF, conserva
el [documento fuente](report/fuentes/TF_1ASI0657_202610_NRC_7.pdf) y distingue
arquitectura propuesta, evidencias originales y verificaciones de esta entrega.
El README anterior se conserva en [histórico](report/historico/README_hito1.md).

El incremento implementa ingresos/egresos, idempotencia, consulta por usuario
y resumen mensual. Identidad real, presupuestos, alertas, IA, cursos e IoT siguen
pendientes. `landing` y `mobile` se reservan para futuros proyectos, como indicó
el usuario.

## Validación y ZIP

Con las dependencias instaladas:

```powershell
cd back
python -m pytest -q
python ../scripts/verificar.py
cd ..
python scripts/empaquetar.py
```

El empaquetado genera un ZIP por componente y un ZIP completo en `entregables/`.
Las bases de ejecución, cachés, entornos y metadatos Git quedan excluidos.
La [evidencia de validación](report/evidencias/validacion.md) documenta los
resultados locales. El workflow de GitHub permite repetir las comprobaciones;
su existencia no demuestra que un despliegue en nube haya sido realizado.
