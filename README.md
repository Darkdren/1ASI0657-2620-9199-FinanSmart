# FinanZen

Los proyectos actuales se gestionan en **cinco repositorios independientes** de
la organización del curso.

## Enlace común

**[Ver todos los repositorios de FinanZen](https://github.com/orgs/1ASI0657-2620-9199/repositories)**

| Repositorio | Contenido | Estado |
| --- | --- | --- |
| [back](https://github.com/1ASI0657-2620-9199/back) | API FastAPI y persistencia SQLite | Primer incremento funcional |
| [report](https://github.com/1ASI0657-2620-9199/report) | Informe actualizado, PDF original, diagramas y evidencias | Actualizado |
| [landing](https://github.com/1ASI0657-2620-9199/landing) | Presentación pública del producto | Repositorio preparado; código pendiente |
| [front](https://github.com/1ASI0657-2620-9199/front) | Panel web HTML, CSS y JavaScript | Funcional |
| [mobile](https://github.com/1ASI0657-2620-9199/mobile) | Aplicación móvil | Repositorio preparado; código pendiente |

Cada repositorio tiene su propio historial Git, README y remoto. El informe y
las instrucciones actuales están en esos repositorios.

## Ejecutar el MVP

Clonar backend y frontend como repositorios vecinos:

```powershell
git clone https://github.com/1ASI0657-2620-9199/back.git
git clone https://github.com/1ASI0657-2620-9199/front.git
cd back
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Interfaz: http://127.0.0.1:8000. Swagger: http://127.0.0.1:8000/docs.

## Antecedente

Este repositorio personal conserva la organización inicial del proyecto y su
historial. El desarrollo vigente corresponde a los cinco repositorios de la
organización enlazada arriba.
