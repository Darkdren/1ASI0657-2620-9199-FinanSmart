# FinanZen — Front

Panel web funcional del MVP, desarrollado con HTML, CSS y JavaScript.
No requiere Node.js ni compilación.

## Contenido

- `index.html`: resumen, tabla de movimientos, análisis y formulario.
- `styles.css`: estilos y adaptación a pantallas pequeñas.
- `app.js`: consultas a la API, presentación de datos y eventos.

## Ejecutar

Desde la raíz del repositorio:

```powershell
cd back
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Abrir http://127.0.0.1:8000. El backend encuentra automáticamente `../front` y
sirve los archivos y la API desde el mismo origen. Si la carpeta está en otra
ubicación, configurar `FINANZEN_FRONTEND_PATH` antes de arrancar el backend.

La interfaz necesita la API para registrar y consultar movimientos; abrir
`index.html` directamente como archivo no conecta el servicio.

## Funcionalidades actuales

- Resumen mensual de ingresos, gastos, saldo y número de movimientos.
- Tabla filtrada por mes y gráfico de gastos por categoría.
- Registro de ingresos y gastos mediante un formulario modal.
- Estado de conexión, mensajes de error y navegación adaptable.

Configuración de demostración: usuario `demo-user`, moneda `PEN` y cuenta
`cash-account`. Cada intento de registro genera una clave de idempotencia UUID.
No hay inicio de sesión, proyecciones de IA, cursos ni alertas de presupuesto.

La aplicación web es distinta de la [landing pendiente](../landing/README.md)
y de la [aplicación móvil pendiente](../mobile/README.md).
