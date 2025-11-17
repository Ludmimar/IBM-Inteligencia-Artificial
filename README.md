# 🎓 IBM - Inteligencia Artificial

> Repositorio de proyectos y ejercicios del programa de Inteligencia Artificial de IBM

<p align="center">
  <img src="https://img.shields.io/badge/IBM-Inteligencia_Artificial-0F62FE?style=for-the-badge&logo=ibm" alt="IBM AI"/>
  <img src="https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/>
</p>

---

## 📋 Tabla de Contenidos

- [Acerca del Proyecto](#-acerca-del-proyecto)
- [Sprint 1: Tienda Aurelion - Sistema Básico](#-sprint-1-tienda-aurelion-sistema-básico)
- [Sprint 2: Tienda Aurelion - Sistema Avanzado con Análisis Estadístico](#-sprint-2-tienda-aurelion-sistema-avanzado-con-análisis-estadístico)
- [Inicio Rápido](#-inicio-rápido)
- [Estructura del Repositorio](#-estructura-del-repositorio)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Autor](#-autor)

---

## 🎯 Acerca del Proyecto

Este repositorio contiene los proyectos desarrollados durante el programa de **Introducción a la Inteligencia Artificial** de IBM. Cada sprint incluye aplicaciones prácticas, análisis de datos y documentación técnica completa.

### Objetivos de Aprendizaje

- ✅ Estructuración y análisis de datos
- ✅ Desarrollo de aplicaciones interactivas en Python
- ✅ Implementación de interfaces web modernas
- ✅ Visualización de datos y dashboards
- ✅ Documentación técnica profesional
- ✅ Evaluación crítica de herramientas de IA

---

## ⚔️ Sprint 1: Tienda Aurelion - Sistema Básico

**Sistema de Gestión de Inventario para Tienda de Fantasía Medieval**

### Descripción

Aplicación completa para gestionar el inventario de la Tienda Aurelion, desarrollada en **3 versiones diferentes**:

1. **🖥️ Programa de Consola** - Interfaz interactiva de línea de comandos
2. **🌐 Aplicación Web Streamlit** - Dashboard profesional con gráficos interactivos ⭐
3. **📓 Jupyter Notebook** - Documentación interactiva con código ejecutable

### Características Principales

- 🔍 Búsqueda avanzada (por categoría, nombre, precio, proveedor)
- 📊 Estadísticas en tiempo real
- ➕ Gestión de productos (agregar, actualizar stock)
- ⚠️ Alertas de bajo inventario
- 📈 Visualizaciones interactivas
- 💾 Persistencia en CSV

### 🚀 Demo Rápida

```bash
# Opción 1: Aplicación Web (Recomendado)
cd "Sprint-1"
pip install streamlit pandas
streamlit run programas/app_streamlit.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

```bash
# Opción 2: Programa de Consola (Sin instalaciones)
cd "Sprint-1"
python programas/tienda_aurelion.py
```

### 📚 Documentación Completa

Toda la documentación del Sprint 1 está disponible en la carpeta correspondiente:

- 📄 **[README.md](Sprint-1/README.md)** - Documentación completa del proyecto
- 📄 **[INICIO_RAPIDO.md](Sprint-1/INICIO_RAPIDO.md)** - Guía de inicio rápido
- 📄 **[INSTRUCCIONES.md](Sprint-1/INSTRUCCIONES.md)** - Instrucciones detalladas de uso
- 📄 **[RESUMEN_FINAL.md](Sprint-1/RESUMEN_FINAL.md)** - Resumen ejecutivo

#### Documentación Técnica

- 📁 **[documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md](Sprint-1/documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md)** - Algoritmos y 6 diagramas de flujo
- 📁 **[documentacion/SUGERENCIAS_COPILOT.md](Sprint-1/documentacion/SUGERENCIAS_COPILOT.md)** - 20 sugerencias de IA evaluadas
- 📁 **[documentacion/GUIA_POWER_BI.md](Sprint-1/documentacion/GUIA_POWER_BI.md)** - Guía para crear dashboard
- 📁 **[documentacion/GUIA_PRESENTACION.md](Sprint-1/documentacion/GUIA_PRESENTACION.md)** - Guía para presentaciones
- 📁 **[documentacion/INSTRUCCIONES_STREAMLIT.md](Sprint-1/documentacion/INSTRUCCIONES_STREAMLIT.md)** - Guía de la app web

### 📊 Estadísticas del Proyecto

- **Base de datos:** 20 productos, 10 categorías, 9 proveedores
- **Líneas de código:** ~1,200+ (Python)
- **Archivos:** 14 archivos principales
- **Documentación:** 8 archivos Markdown (~50 páginas)
- **Diagramas:** 6 diagramas de flujo
- **Dependencias externas:** 0 (versión consola) / 2 (versión web)

---

## ⚔️ Sprint 2: Tienda Aurelion - Sistema Avanzado con Análisis Estadístico

**Sistema de Gestión de Inventario y Ventas con Base de Datos Normalizada**

### Descripción

Evolución del Sprint 1 con mejoras significativas: base de datos normalizada, gestión de clientes y ventas, y análisis estadístico completo.

### Nuevas Características

- 🗄️ **Base de datos normalizada** con 4 tablas relacionadas:
  - `productos.csv` - 80 productos
  - `clientes.csv` - 50 clientes
  - `ventas.csv` - 100 ventas
  - `detalle_ventas.csv` - 273 detalles de ventas
- 👥 **Gestión completa de clientes** con estadísticas
- 💰 **Sistema de ventas** con detalle de transacciones
- 📊 **Dashboard Power BI Desktop profesional**:
  - Archivo `.pbix` completo listo para usar ⭐
  - Plantilla `.pbit` para personalizar
  - 8 KPIs principales con visualizaciones interactivas
  - Filtros dinámicos y cross-filtering automático
  - Tema medieval personalizado
  - Guía paso a paso de creación incluida
  - Integrado con la aplicación Streamlit
- 📊 **Análisis estadístico completo**:
  - Estadísticas descriptivas básicas
  - Identificación de distribución de variables
  - Análisis de correlaciones entre variables principales
  - Detección de outliers (valores extremos)
  - 3 gráficos representativos generados automáticamente
  - Interpretación de resultados orientada al problema
  - **Análisis integrado en Streamlit** con descripciones detalladas en cada gráfico ⭐

### 🚀 Demo Rápida

```bash
# Opción 1: Aplicación Web Streamlit (Recomendado)
cd "Sprint-2"
pip install streamlit pandas numpy matplotlib seaborn scipy
streamlit run programas/app_streamlit.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

```bash
# Opción 2: Dashboard Power BI Desktop (Profesional) ⭐
cd "Sprint-2"
# Opción A: Abrir archivo completo (.pbix)
start Tienda_Aurelion_Dashboard_Sprint2.pbix

# Opción B: Usar plantilla (.pbit)
start Tienda_Aurelion_Dashboard_Sprint2.pbit
```

**Requisito:** Microsoft Power BI Desktop (gratis) - [Descargar aquí](https://powerbi.microsoft.com/desktop/)

```bash
# Opción 3: Análisis Estadístico Completo
cd "Sprint-2"
python programas/analisis_estadistico.py
```

Esto generará:
- Análisis completo en consola
- 3 gráficos profesionales en `graficos/`

```bash
# Opción 4: Análisis Estadístico en Jupyter (Interactivo)
cd "Sprint-2"
jupyter notebook programas/analisis_estadistico.ipynb
```

Interfaz interactiva con código ejecutable y visualizaciones integradas.

```bash
# Opción 5: Programa de Consola (Sin instalaciones)
cd "Sprint-2"
python programas/tienda_aurelion.py
```

### 📚 Documentación Completa

Toda la documentación del Sprint 2 está disponible en la carpeta correspondiente:

- 📄 **[README.md](Sprint-2/README.md)** - Documentación completa del proyecto
- 📄 **[INICIO_RAPIDO.md](Sprint-2/INICIO_RAPIDO.md)** - Guía de inicio rápido
- 📄 **[INSTRUCCIONES.md](Sprint-2/INSTRUCCIONES.md)** - Instrucciones detalladas de uso
- 📄 **[RESUMEN_FINAL.md](Sprint-2/RESUMEN_FINAL.md)** - Resumen ejecutivo

#### Documentación Técnica

- 📁 **[documentacion/ANALISIS_ESTADISTICO.md](Sprint-2/documentacion/ANALISIS_ESTADISTICO.md)** ⭐ - Análisis estadístico completo
- 📁 **[documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md](Sprint-2/documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md)** ⭐⭐ - Guía paso a paso del dashboard Power BI
- 📁 **[documentacion/COMO_CREAR_DASHBOARD_POWERBI.md](Sprint-2/documentacion/COMO_CREAR_DASHBOARD_POWERBI.md)** - Guía maestra de Power BI
- 📁 **[documentacion/CHECKLIST_DASHBOARD.md](Sprint-2/documentacion/CHECKLIST_DASHBOARD.md)** - Lista de verificación del dashboard
- 📁 **[documentacion/LAYOUT_VISUAL_DASHBOARD.md](Sprint-2/documentacion/LAYOUT_VISUAL_DASHBOARD.md)** - Vista previa visual
- 📁 **[documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md](Sprint-2/documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md)** - Algoritmos y diagramas de flujo
- 📁 **[documentacion/SUGERENCIAS_COPILOT.md](Sprint-2/documentacion/SUGERENCIAS_COPILOT.md)** - Sugerencias de IA evaluadas
- 📁 **[documentacion/GUIA_POWER_BI.md](Sprint-2/documentacion/GUIA_POWER_BI.md)** - Guía general de Power BI
- 📁 **[documentacion/GUIA_PRESENTACION.md](Sprint-2/documentacion/GUIA_PRESENTACION.md)** - Guía para presentaciones
- 📁 **[documentacion/INSTRUCCIONES_STREAMLIT.md](Sprint-2/documentacion/INSTRUCCIONES_STREAMLIT.md)** - Guía de la app web

### 📊 Estadísticas del Proyecto

- **Base de datos:** 4 archivos CSV normalizados
  - 80 productos, 50 clientes, 100 ventas, 273 detalles
  - Ingresos totales: 231,485 monedas
  - Valor inventario: 1,909,400 monedas
  - Stock total: 4,585 unidades
- **Dashboard Power BI:** ⭐
  - 2 archivos (.pbix y .pbit)
  - 8 KPIs principales
  - 10+ visualizaciones interactivas
  - Filtros dinámicos y cross-filtering
  - 8 queries M (4 con rutas absolutas, 4 con relativas)
  - 8 medidas DAX (2 versiones: completas y simplificadas)
  - Tema medieval personalizado
- **Líneas de código:** ~2,500+ (Python) + ~200 (DAX/M)
- **Archivos:** 25+ archivos principales
- **Documentación:** 15+ archivos Markdown (~100 páginas)
- **Gráficos:** 3 gráficos profesionales generados + visualizaciones interactivas en Streamlit + Dashboard Power BI
- **Análisis estadístico:** Completo con correlaciones y outliers, integrado en la aplicación web
- **Dependencias externas:** 0 (versión consola) / 7 (versión completa)

---

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.6 o superior
- Git (opcional, para clonar el repositorio)

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/IBM-Inteligencia-Artificial.git
   cd IBM-Inteligencia-Artificial
   ```

2. **Elegir Sprint**
   ```bash
   # Sprint 1 - Sistema básico
   cd "Sprint-1"
   
   # Sprint 2 - Sistema avanzado con análisis estadístico
   cd "Sprint-2"
   ```

3. **Instalar dependencias**
   ```bash
   # Para Sprint 1 (solo aplicación web)
   pip install streamlit pandas

   # Para Sprint 2 (aplicación web + análisis estadístico)
   pip install streamlit pandas numpy matplotlib seaborn scipy

   # O instalar todas las dependencias desde requirements.txt
   pip install -r requirements.txt
   ```

4. **Ejecutar el proyecto**
   ```bash
   # Sprint 1 o Sprint 2 - Aplicación web (recomendado)
   streamlit run programas/app_streamlit.py

   # Sprint 1 o Sprint 2 - Programa de consola (sin instalaciones)
   python programas/tienda_aurelion.py

   # Sprint 2 - Análisis estadístico completo
   python programas/analisis_estadistico.py
   ```

---

## 📁 Estructura del Repositorio

```
IBM-Inteligencia-Artificial/
│
├── 📄 README.md                        (este archivo)
│
├── Sprint-1/                           Sprint 1 - Sistema Básico
│   ├── 📄 README.md                    Documentación principal
│   ├── 📄 INICIO_RAPIDO.md             Guía de inicio rápido
│   ├── 📄 INSTRUCCIONES.md             Instrucciones de uso
│   ├── 📄 RESUMEN_FINAL.md             Resumen ejecutivo
│   ├── 📄 requirements.txt             Dependencias
│   │
│   ├── datos/                          Base de datos
│   │   ├── tienda_aurelion.csv         20 productos
│   │   └── tienda_aurelion.pbix        Dashboard Power BI
│   │
│   ├── programas/                      Código fuente
│   │   ├── tienda_aurelion.py          Programa de consola
│   │   ├── app_streamlit.py            Aplicación web ⭐
│   │   └── tienda_aurelion.ipynb       Jupyter Notebook
│   │
│   ├── documentacion/                  Documentación técnica
│   │   ├── INDICE_PROYECTO.md
│   │   ├── PSEUDOCODIGO_Y_DIAGRAMAS.md
│   │   ├── SUGERENCIAS_COPILOT.md
│   │   ├── GUIA_POWER_BI.md
│   │   ├── GUIA_PRESENTACION.md
│   │   └── INSTRUCCIONES_STREAMLIT.md
│   │
│   └── Power BI/                       Recursos Power BI
│       ├── README.md
│       ├── measures.dax
│       ├── query.m
│       ├── theme.json
│       └── layout_instructions.md
│
└── Sprint-2/                           Sprint 2 - Sistema Avanzado
    ├── 📄 README.md                    Documentación principal
    ├── 📄 INICIO_RAPIDO.md             Guía de inicio rápido
    ├── 📄 INSTRUCCIONES.md             Instrucciones de uso
    ├── 📄 RESUMEN_FINAL.md             Resumen ejecutivo
    ├── 📄 ORGANIZACION_ARCHIVOS.md     Estructura del proyecto ⭐
    ├── 📄 requirements.txt             Dependencias
    ├── 📄 .gitignore                   Configuración de Git
    ├── 📄 Tienda_Aurelion_Dashboard_Sprint2.pbix  Dashboard Power BI completo ⭐⭐
    ├── 📄 Tienda_Aurelion_Dashboard_Sprint2.pbit  Plantilla Power BI ⭐⭐
    │
    ├── datos/                          Base de datos normalizada
    │   ├── productos.csv               80 productos
    │   ├── clientes.csv                50 clientes
    │   ├── ventas.csv                  100 ventas
    │   └── detalle_ventas.csv          273 detalles de ventas
    │
    ├── programas/                      Código fuente (6 versiones)
    │   ├── tienda_aurelion.py          Programa de consola mejorado
    │   ├── app_streamlit.py            Aplicación web mejorada ⭐
    │   ├── tienda_aurelion.ipynb       Jupyter Notebook
    │   ├── analisis_estadistico.py     Análisis estadístico completo ⭐
    │   ├── analisis_estadistico.ipynb  Notebook de análisis estadístico ⭐⭐
    │   └── validar_datos_powerbi.py    Validador de datos para Power BI
    │
    ├── graficos/                       Gráficos generados automáticamente
    │   ├── grafico1_distribucion_precios.png
    │   ├── grafico2_matriz_correlacion.png
    │   └── grafico3_outliers_ventas.png
    │
    ├── documentacion/                  Documentación técnica (12 guías)
    │   ├── INDICE_PROYECTO.md
    │   ├── ANALISIS_ESTADISTICO.md     Análisis completo ⭐
    │   ├── GUIA_RAPIDA_DASHBOARD_POWERBI.md  Guía paso a paso Power BI ⭐⭐
    │   ├── COMO_CREAR_DASHBOARD_POWERBI.md   Guía maestra Power BI
    │   ├── CHECKLIST_DASHBOARD.md      Lista de verificación
    │   ├── LAYOUT_VISUAL_DASHBOARD.md  Vista previa visual
    │   ├── RESUMEN_DASHBOARD_POWERBI.md  Resumen del dashboard
    │   ├── PSEUDOCODIGO_Y_DIAGRAMAS.md
    │   ├── SUGERENCIAS_COPILOT.md
    │   ├── GUIA_POWER_BI.md            Guía general
    │   ├── GUIA_PRESENTACION.md
    │   └── INSTRUCCIONES_STREAMLIT.md
    │
    └── Power BI/                       Recursos Power BI (completos) ⭐⭐
        ├── README.md
        ├── measures.dax                Medidas DAX originales
        ├── measures_SIMPLIFICADAS.dax  Medidas DAX simplificadas
        ├── measures_SIN_COLUMNAS_CALCULADAS.dax  Medidas sin dependencias
        ├── query_productos.m           Query productos (relativa)
        ├── query_clientes.m            Query clientes (relativa)
        ├── query_ventas.m              Query ventas (relativa)
        ├── query_detalle_ventas.m      Query detalles (relativa)
        ├── query_productos_RUTA_ABSOLUTA.m     Query productos (absoluta)
        ├── query_clientes_RUTA_ABSOLUTA.m      Query clientes (absoluta)
        ├── query_ventas_RUTA_ABSOLUTA.m        Query ventas (absoluta)
        ├── query_detalle_ventas_RUTA_ABSOLUTA.m  Query detalles (absoluta)
        ├── theme.json                  Tema medieval personalizado
        ├── layout_instructions.md      Instrucciones de layout
        └── Sprint2.pbit                Plantilla alternativa
```

---

## 🛠️ Tecnologías Utilizadas

### Lenguajes

- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) Python 3.6+
- ![DAX](https://img.shields.io/badge/DAX-F2C811?style=flat&logo=powerbi&logoColor=black) DAX (Power BI)

### Frameworks y Librerías

- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) Streamlit - Aplicación web
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) Pandas - Análisis de datos
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) NumPy - Cálculos numéricos (Sprint 2)
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white) Matplotlib - Visualización (Sprint 2)
- ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=python&logoColor=white) Seaborn - Visualización estadística (Sprint 2)
- ![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white) SciPy - Análisis estadístico (Sprint 2)
- ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white) Jupyter - Notebooks interactivos

### Herramientas

- ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black) Power BI - Visualización de datos
- ![CSV](https://img.shields.io/badge/CSV-217346?style=flat&logo=microsoftexcel&logoColor=white) CSV - Almacenamiento de datos
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) Git - Control de versiones

---

## 📖 Recursos Adicionales

### Sprint 1 - Para Empezar

- **Nueva en el proyecto?** → Lee [Sprint-1/INICIO_RAPIDO.md](Sprint-1/INICIO_RAPIDO.md)
- **Quieres ejecutar el programa?** → Lee [Sprint-1/INSTRUCCIONES.md](Sprint-1/INSTRUCCIONES.md)
- **Buscas documentación completa?** → Lee [Sprint-1/README.md](Sprint-1/README.md)

### Sprint 2 - Para Empezar

- **Nueva en el proyecto?** → Lee [Sprint-2/INICIO_RAPIDO.md](Sprint-2/INICIO_RAPIDO.md)
- **Quieres ejecutar el programa?** → Lee [Sprint-2/INSTRUCCIONES.md](Sprint-2/INSTRUCCIONES.md)
- **Quieres crear el dashboard Power BI?** → Lee [Sprint-2/documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md](Sprint-2/documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md) ⭐⭐
- **Buscas análisis estadístico?** → Lee [Sprint-2/documentacion/ANALISIS_ESTADISTICO.md](Sprint-2/documentacion/ANALISIS_ESTADISTICO.md) ⭐
- **Buscas documentación completa?** → Lee [Sprint-2/README.md](Sprint-2/README.md)

### Para Desarrolladores

- **Entender la lógica?** → [Sprint-1/documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md](Sprint-1/documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md) o [Sprint-2/documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md](Sprint-2/documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md)
- **Análisis de decisiones técnicas?** → [Sprint-1/documentacion/SUGERENCIAS_COPILOT.md](Sprint-1/documentacion/SUGERENCIAS_COPILOT.md) o [Sprint-2/documentacion/SUGERENCIAS_COPILOT.md](Sprint-2/documentacion/SUGERENCIAS_COPILOT.md)
- **Guía de Streamlit?** → [Sprint-1/documentacion/INSTRUCCIONES_STREAMLIT.md](Sprint-1/documentacion/INSTRUCCIONES_STREAMLIT.md) o [Sprint-2/documentacion/INSTRUCCIONES_STREAMLIT.md](Sprint-2/documentacion/INSTRUCCIONES_STREAMLIT.md)

### Para Presentaciones y Dashboards

- **Crear dashboard en Power BI (Sprint 1)?** → [Sprint-1/documentacion/GUIA_POWER_BI.md](Sprint-1/documentacion/GUIA_POWER_BI.md)
- **Crear dashboard en Power BI (Sprint 2 - Completo)?** → [Sprint-2/documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md](Sprint-2/documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md) ⭐⭐
- **Usar dashboard Power BI ya creado (Sprint 2)?** → Abre `Sprint-2/Tienda_Aurelion_Dashboard_Sprint2.pbix` ⭐
- **Preparar presentación oral?** → [Sprint-1/documentacion/GUIA_PRESENTACION.md](Sprint-1/documentacion/GUIA_PRESENTACION.md) o [Sprint-2/documentacion/GUIA_PRESENTACION.md](Sprint-2/documentacion/GUIA_PRESENTACION.md)

---

## 🎓 Habilidades Demostradas

### Programación
- ✅ Desarrollo en Python con mejores prácticas
- ✅ Programación orientada a objetos
- ✅ Manejo de archivos y persistencia de datos
- ✅ Validación de datos y manejo de errores
- ✅ Desarrollo web con Streamlit

### Análisis de Datos

- ✅ Estructuración de datasets
- ✅ Estadísticas descriptivas (Sprint 1)
- ✅ Análisis estadístico avanzado (Sprint 2):
  - Identificación de distribuciones
  - Análisis de correlaciones
  - Detección de outliers
  - Interpretación de resultados
- ✅ Visualización de datos
- ✅ Dashboard interactivos
- ✅ Gráficos profesionales con matplotlib/seaborn (Sprint 2)

### Inteligencia Artificial
- ✅ Evaluación crítica de sugerencias de IA
- ✅ Decisiones técnicas fundamentadas
- ✅ Comprensión de trade-offs tecnológicos

### Soft Skills
- ✅ Documentación técnica profesional
- ✅ Comunicación clara y efectiva
- ✅ Pensamiento analítico
- ✅ Resolución de problemas

---

## 👨‍💻 Autor

**Martos Ludmila**
- DNI: 34811650
- Programa: Introducción a la Inteligencia Artificial
- Institución: IBM
- Año: 2025

---

## 📝 Notas del Proyecto

### Sprint 1 - Tienda Aurelion (Sistema Básico)

Este proyecto demuestra la aplicación práctica de conceptos de programación, análisis de datos y desarrollo de aplicaciones. Incluye:

- 🎨 **3 interfaces diferentes** (consola, web, notebook)
- 📊 **Base de datos completa** con 20 productos
- 📚 **Documentación exhaustiva** (~50 páginas)
- 🔍 **Análisis crítico** de 20 sugerencias de IA
- 📈 **Visualizaciones interactivas** con Streamlit
- 💾 **Código limpio** y bien documentado

### Sprint 2 - Tienda Aurelion (Sistema Avanzado)

Evolución del Sprint 1 con mejoras significativas:

- 🗄️ **Base de datos normalizada** con 4 tablas relacionadas (80 productos, 50 clientes, 100 ventas)
- 👥 **Gestión de clientes** completa con estadísticas y análisis
- 💰 **Sistema de ventas** con detalle de transacciones (273 detalles)
- 📊 **Dashboard Power BI Desktop profesional** ⭐⭐:
  - Archivo `.pbix` completo listo para usar
  - Plantilla `.pbit` para personalizar
  - 8 KPIs principales (Valor Inventario, Stock Total, Ingresos, etc.)
  - 10+ visualizaciones interactivas (gráficos, tablas, tarjetas)
  - Filtros dinámicos por categoría y ciudad
  - Cross-filtering automático entre visuales
  - Tema medieval personalizado (colores oro, rojo oscuro, azul marino)
  - Guía paso a paso completa de creación
  - Integrado en la aplicación Streamlit
  - 8 queries M (4 con rutas relativas + 4 con absolutas)
  - 3 versiones de medidas DAX (originales, simplificadas, sin columnas calculadas)
- 📊 **Análisis estadístico completo**:
  - Estadísticas descriptivas básicas
  - Identificación de distribución de variables
  - Análisis de correlaciones entre variables principales
  - Detección de outliers (valores extremos)
  - 3 gráficos representativos generados automáticamente
  - Interpretación de resultados orientada al problema
  - **Integrado en Streamlit** con descripciones detalladas en cada gráfico ⭐
- 📈 **Visualizaciones avanzadas** con matplotlib y seaborn
- 🔍 **Búsqueda mejorada** con relaciones entre tablas
- 📚 **Documentación ampliada** (~100 páginas)
- 🎨 **Todas las apps mencionan Power BI** (Streamlit, consola, notebooks)

### Próximos Sprints

Este repositorio se actualizará con nuevos proyectos a medida que avance el programa de IBM.

---

## 🌟 Características Destacadas

| Aspecto | Sprint 1 | Sprint 2 |
|---------|----------|----------|
| **Versiones** | 3 (Consola, Web, Notebook) | 6 (Consola, Web, Notebook, Análisis Python, Análisis Notebook, **Power BI Desktop**) ⭐ |
| **Base de Datos** | 1 archivo CSV (20 productos) | 4 archivos CSV normalizados (80 productos, 50 clientes, 100 ventas) |
| **Gestión de Clientes** | ❌ | ✅ Completa |
| **Sistema de Ventas** | ❌ | ✅ Completo con detalles |
| **Análisis Estadístico** | Básico | ✅ Completo + Integrado en Streamlit |
| **Interfaz Web** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ Mejorada con análisis estadístico |
| **Dashboard Power BI** | Guía básica | ✅ **Dashboard completo (.pbix + .pbit)** con 8 KPIs y 10+ visualizaciones ⭐⭐ |
| **Documentación** | ⭐⭐⭐⭐⭐ (~50 páginas) | ⭐⭐⭐⭐⭐ Ampliada (~100 páginas) |
| **Código** | ⭐⭐⭐⭐⭐ (~1,200 líneas) | ⭐⭐⭐⭐⭐ (~2,700+ líneas Python + DAX/M) |
| **Gráficos** | Interactivos básicos | Profesionales + Descripciones detalladas + Power BI |
| **Escalabilidad** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **UX** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Queries Power BI** | 1 query básica | 8 queries M (4 relativas + 4 absolutas) + 8 medidas DAX (3 versiones) |

---

## 📞 Soporte

### Problemas Comunes

#### "No se encuentra el archivo CSV"
```bash
# Sprint 1: Asegúrate de estar en la carpeta correcta
cd "Sprint-1"
# Verifica que existe el archivo
dir datos\tienda_aurelion.csv  # Windows
ls datos/tienda_aurelion.csv   # Linux/Mac

# Sprint 2: Verifica que existen los 4 archivos CSV
cd "Sprint-2"
dir datos\*.csv  # Windows - debería mostrar productos.csv, clientes.csv, ventas.csv, detalle_ventas.csv
ls datos/*.csv   # Linux/Mac
```

#### "python no se reconoce como comando"
```bash
# Intenta con python3
python3 programas/tienda_aurelion.py

# O en Windows
py programas/tienda_aurelion.py
```

#### "streamlit: comando no encontrado"
```bash
# Instala Streamlit primero
pip install streamlit pandas
```

Para más ayuda, consulta la documentación completa:
- Sprint 1: [Sprint-1/README.md](Sprint-1/README.md)
- Sprint 2: [Sprint-2/README.md](Sprint-2/README.md)

---

## 📜 Licencia

Este proyecto es parte del programa educativo de IBM y está destinado únicamente para fines de aprendizaje.

---

## 👨‍💻 Autor

**Desarrollador**: Ludmila Martos

## 📞 Contacto

- **Email**: [ludmilamartos@gmail.com](mailto:ludmilamartos@gmail.com)
- **LinkedIn**: [ludmimar89](https://www.linkedin.com/in/ludmimar89/)
- **GitHub**: [Ludmimar](https://github.com/Ludmimar)


<p align="center">
  <strong>⚔️ Tienda Aurelion - Donde la magia y la tecnología se encuentran ✨</strong>
</p>

<p align="center">
  Hecho con ❤️ para IBM - Inteligencia Artificial
</p>

---

**Última actualización:** Noviembre 2025  
**Versión:** 2.5 - Power BI Desktop Edition  
**Estado:** ✅ Sprint 1 Completo | ✅ Sprint 2 Completo con Dashboard Power BI Profesional ⭐⭐

### 📈 Últimas Actualizaciones (Sprint 2 - Noviembre 2025)

- ✅ **Dashboard Power BI Desktop completo:** Archivo `.pbix` y `.pbit` listos para usar ⭐⭐
  - 8 KPIs principales con visualizaciones interactivas
  - 10+ gráficos profesionales (barras, líneas, scatter, donut, tablas)
  - Tema medieval personalizado (oro, rojo oscuro, azul marino)
  - Cross-filtering automático y filtros dinámicos
  - 3 versiones de medidas DAX para diferentes escenarios
  - 8 queries M (relativas y absolutas)
  - Guía paso a paso completa (30 minutos)
  - Integrado en aplicación Streamlit con página dedicada
- ✅ **Todas las apps mencionan Power BI:** Streamlit, consola, notebooks con referencias cruzadas
- ✅ **Base de datos expandida:** 80 productos, 50 clientes, 100 ventas, 273 detalles
- ✅ **Análisis estadístico integrado** en Streamlit con descripciones detalladas en cada gráfico
- ✅ **Documentación reorganizada:** Archivos Power BI en `documentacion/` para mejor organización
- ✅ **Documentación completa** actualizada con todas las estadísticas actuales (~100 páginas)
- ✅ **Notebook de análisis estadístico** (`analisis_estadistico.ipynb`) para análisis interactivo
- ✅ **Sistema de ventas completo** con historial y detalles de transacciones
- ✅ **.gitignore configurado** para entregas limpias del proyecto

