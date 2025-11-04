# Tienda Aurelion — Power BI Template Helper (Completa)

Este paquete contiene los recursos necesarios para **crear rápidamente una plantilla Power BI (.pbit)** con todas las páginas y visuales solicitados (Overview, Análisis de Productos, Proveedores). No se incluye un .pbit porque requiere Power BI Desktop para generarlo, pero con estos archivos lo vas a poder armar en minutos.

## Contenido del paquete
- `query.m` — Script Power Query (M) para cargar `datos/tienda_aurelion.csv` y crear columnas calculadas (`valor_inventario`, `estado_stock`, `rango_precio`).
- `measures.dax` — Medidas DAX listas para pegar en Power BI (Modeling → New Measure).
- `theme.json` — Tema (colores y tipografías) que podés importar en Power BI: View → Themes → Browse for themes.
- `layout_instructions.md` — Instrucciones paso a paso para construir las páginas y visuales exactamente como la guía.
- `README.md` — (este archivo)

## Flujo recomendado (resumen rápido)
1. Abrir Power BI Desktop.
2. Reemplazar el CSV en `datos/tienda_aurelion.csv` (ruta relativa junto al archivo .pbit cuando lo generes).
3. Obtener datos → Blank Query → Advanced Editor → pegar `query.m`.
4. Cargar y aplicar cambios.
5. En Report view: importar `theme.json`.
6. Crear las medidas pegando `measures.dax` (Modeling → New Measure).
7. Seguir `layout_instructions.md` para recrear las páginas (Overview, Productos, Proveedores).
8. Archivo → Export → Power BI template → guardar `.pbit`.
