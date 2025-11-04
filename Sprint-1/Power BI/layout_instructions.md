# Layout e instrucciones para reconstruir el dashboard (completa)

A continuación tenés un paso a paso para recrear las 3 páginas solicitadas: **Overview (General)**, **Análisis de Productos**, **Proveedores**.

---

## Preparación previa
1. Asegurate de tener Power BI Desktop actualizado.
2. Coloca tu CSV en `datos/tienda_aurelion.csv` (carpeta relativa junto al archivo .pbit cuando lo exportes).
3. Abrí Power BI Desktop.

---

## 1) Cargar datos (usar query.m)
1. Home → Get Data → Blank Query
2. Advanced Editor → pegar el contenido de `query.m`
3. Rename query a `Productos`
4. Close & Apply

---

## 2) Importar tema
1. View → Themes → Browse for themes
2. Seleccioná `theme.json`

---

## 3) Crear Measures
1. Modeling → New Measure
2. Copiá las medidas desde `measures.dax`
3. Verifica nombres y referencias a la tabla `Productos` (si tu tabla quedó con otro nombre, adaptalas)

---

## 4) Página 1 — Overview (Overview General)
- Layout: 1 fila superior con 5 tarjetas KPI, zona media con 2 gráficos (Categorias y Top 10), zona inferior con anillo + dispersión y tabla de stock bajo.
- KPIs (usar Card visual):
  - Total de Productos: `COUNTROWS(Productos)` o `COUNT(Productos[id])`
  - Valor Total Inventario: `[Valor Total Inventario]`
  - Stock Total: `[Stock Total]`
  - Categorías Únicas: `DISTINCTCOUNT(Productos[categoria])`
  - Productos con Stock Bajo: `[Productos Stock Bajo]`
- Gráfico de barras: Eje Y = `categoria`, Eje X = `COUNTROWS` o `SUM(Productos[stock])`
- Top 10: Column chart con `nombre` y `Valor por Producto`, aplicar filtro Top N = 10
- Donut: Legend = `categoria`, Value = `SUM(Productos[stock])`
- Scatter: X = `precio`, Y = `stock`, Details = `nombre`, Size = `valor_inventario`
- Tabla: columnas `nombre`, `categoria`, `stock`, `proveedor` con filtro `[stock] <= 20` y formato condicional.

---

## 5) Página 2 — Análisis de Productos
- Top 10 productos más valiosos (Column chart)
- Top 10 productos con más stock (Column chart)
- Scatter detalle precio vs stock con línea de referencia si querés
- Slicers: Rango de precio, Estado de stock, Categoría

---

## 6) Página 3 — Proveedores
- Stacked bar: Eje Y = `proveedor`, Eje X = `COUNT(id)`, Legend = `categoria`
- Tabla por proveedor con `valor_inventario` y `COUNT(id)`
- KPI: Proveedor Líder (medida que devuelve el proveedor con más productos)

---

## 7) Formateo y accesibilidad
- Ordená visuales con suficientes márgenes.
- Aplicá formato condicional en tablas (stock crítico en rojo).
- Agregá tooltips personalizados (Fields → Tooltips; podés crear una página de tooltip y asignarla).
- Añadí una tarjeta con la fecha de última actualización (Home → Transform data → Advanced Editor → podés agregar un parámetro o columna si el CSV trae fecha).

---

## 8) Exportar plantilla (.pbit)
1. File → Export → Power BI template
2. Guardá `Tienda_Aurelion_Dashboard.pbit`
3. Acompañá el .pbit con la carpeta `datos` que contenga `tienda_aurelion.csv` para que al abrir la plantilla Power BI pida el archivo relativo.

---

¡Listo! Con esto tenés todo para generar la plantilla completa en tu Power BI Desktop. Si querés, puedo ahora:
- Generar una **presentación .pptx** que muestre el layout página por página.
- Intentar crear un `.pbix` básico como archivo de ejemplo (solo si subís el CSV aquí).
