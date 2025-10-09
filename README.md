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
- [Sprint 1: Tienda Aurelion](#-sprint-1-tienda-aurelion)
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

## ⚔️ Sprint 1: Tienda Aurelion

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
cd "Sprint 1"
pip install streamlit pandas
streamlit run programas/app_streamlit.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

```bash
# Opción 2: Programa de Consola (Sin instalaciones)
cd "Sprint 1"
python programas/tienda_aurelion.py
```

### 📚 Documentación Completa

Toda la documentación del Sprint 1 está disponible en la carpeta correspondiente:

- 📄 **[README.md](Sprint%201/README.md)** - Documentación completa del proyecto
- 📄 **[INICIO_RAPIDO.md](Sprint%201/INICIO_RAPIDO.md)** - Guía de inicio rápido
- 📄 **[INSTRUCCIONES.md](Sprint%201/INSTRUCCIONES.md)** - Instrucciones detalladas de uso
- 📄 **[RESUMEN_FINAL.md](Sprint%201/RESUMEN_FINAL.md)** - Resumen ejecutivo

#### Documentación Técnica

- 📁 **[documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md](Sprint%201/documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md)** - Algoritmos y 6 diagramas de flujo
- 📁 **[documentacion/SUGERENCIAS_COPILOT.md](Sprint%201/documentacion/SUGERENCIAS_COPILOT.md)** - 20 sugerencias de IA evaluadas
- 📁 **[documentacion/GUIA_POWER_BI.md](Sprint%201/documentacion/GUIA_POWER_BI.md)** - Guía para crear dashboard
- 📁 **[documentacion/GUIA_PRESENTACION.md](Sprint%201/documentacion/GUIA_PRESENTACION.md)** - Guía para presentaciones
- 📁 **[documentacion/INSTRUCCIONES_STREAMLIT.md](Sprint%201/documentacion/INSTRUCCIONES_STREAMLIT.md)** - Guía de la app web

### 📊 Estadísticas del Proyecto

- **Base de datos:** 20 productos, 10 categorías, 9 proveedores
- **Líneas de código:** ~1,200+ (Python)
- **Archivos:** 14 archivos principales
- **Documentación:** 8 archivos Markdown (~50 páginas)
- **Diagramas:** 6 diagramas de flujo
- **Dependencias externas:** 0 (versión consola) / 2 (versión web)

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

2. **Navegar al Sprint 1**
   ```bash
   cd "Sprint 1"
   ```

3. **Instalar dependencias (opcional)**
   ```bash
   # Para la aplicación web
   pip install streamlit pandas

   # O instalar todas las dependencias
   pip install -r requirements.txt
   ```

4. **Ejecutar el proyecto**
   ```bash
   # Aplicación web (recomendado)
   streamlit run programas/app_streamlit.py

   # O programa de consola (sin instalaciones)
   python programas/tienda_aurelion.py
   ```

---

## 📁 Estructura del Repositorio

```
IBM-Inteligencia-Artificial/
│
├── 📄 README.md                        (este archivo)
│
└── Sprint 1/                           Sprint 1 - Tienda Aurelion
    ├── 📄 README.md                    Documentación principal
    ├── 📄 INICIO_RAPIDO.md             Guía de inicio rápido
    ├── 📄 INSTRUCCIONES.md             Instrucciones de uso
    ├── 📄 RESUMEN_FINAL.md             Resumen ejecutivo
    ├── 📄 requirements.txt             Dependencias
    │
    ├── datos/                          Base de datos
    │   ├── tienda_aurelion.csv         20 productos
    │   └── tienda_aurelion.pbix        Dashboard Power BI
    │
    ├── programas/                      Código fuente
    │   ├── tienda_aurelion.py          Programa de consola
    │   ├── app_streamlit.py            Aplicación web ⭐
    │   └── tienda_aurelion.ipynb       Jupyter Notebook
    │
    ├── documentacion/                  Documentación técnica
    │   ├── INDICE_PROYECTO.md
    │   ├── PSEUDOCODIGO_Y_DIAGRAMAS.md
    │   ├── SUGERENCIAS_COPILOT.md
    │   ├── GUIA_POWER_BI.md
    │   ├── GUIA_PRESENTACION.md
    │   └── INSTRUCCIONES_STREAMLIT.md
    │
    └── Power BI/                       Recursos Power BI
        ├── README.md
        ├── measures.dax
        ├── query.m
        ├── theme.json
        └── layout_instructions.md
```

---

## 🛠️ Tecnologías Utilizadas

### Lenguajes

- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) Python 3.6+
- ![DAX](https://img.shields.io/badge/DAX-F2C811?style=flat&logo=powerbi&logoColor=black) DAX (Power BI)

### Frameworks y Librerías

- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) Streamlit - Aplicación web
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) Pandas - Análisis de datos
- ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white) Jupyter - Notebooks interactivos

### Herramientas

- ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black) Power BI - Visualización de datos
- ![CSV](https://img.shields.io/badge/CSV-217346?style=flat&logo=microsoftexcel&logoColor=white) CSV - Almacenamiento de datos
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) Git - Control de versiones

---

## 📖 Recursos Adicionales

### Para Empezar

- **Nueva en el proyecto?** → Lee [Sprint 1/INICIO_RAPIDO.md](Sprint%201/INICIO_RAPIDO.md)
- **Quieres ejecutar el programa?** → Lee [Sprint 1/INSTRUCCIONES.md](Sprint%201/INSTRUCCIONES.md)
- **Buscas documentación completa?** → Lee [Sprint 1/README.md](Sprint%201/README.md)

### Para Desarrolladores

- **Entender la lógica?** → [documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md](Sprint%201/documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md)
- **Análisis de decisiones técnicas?** → [documentacion/SUGERENCIAS_COPILOT.md](Sprint%201/documentacion/SUGERENCIAS_COPILOT.md)
- **Guía de Streamlit?** → [documentacion/INSTRUCCIONES_STREAMLIT.md](Sprint%201/documentacion/INSTRUCCIONES_STREAMLIT.md)

### Para Presentaciones

- **Crear dashboard en Power BI?** → [documentacion/GUIA_POWER_BI.md](Sprint%201/documentacion/GUIA_POWER_BI.md)
- **Preparar presentación oral?** → [documentacion/GUIA_PRESENTACION.md](Sprint%201/documentacion/GUIA_PRESENTACION.md)

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
- ✅ Estadísticas descriptivas
- ✅ Visualización de datos
- ✅ Dashboard interactivos

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

### Sprint 1 - Tienda Aurelion

Este proyecto demuestra la aplicación práctica de conceptos de programación, análisis de datos y desarrollo de aplicaciones. Incluye:

- 🎨 **3 interfaces diferentes** (consola, web, notebook)
- 📊 **Base de datos completa** con 20 productos
- 📚 **Documentación exhaustiva** (~50 páginas)
- 🔍 **Análisis crítico** de 20 sugerencias de IA
- 📈 **Visualizaciones interactivas** con Streamlit
- 💾 **Código limpio** y bien documentado

### Próximos Sprints

Este repositorio se actualizará con nuevos proyectos a medida que avance el programa de IBM.

---

## 🌟 Características Destacadas

| Aspecto | Implementación |
|---------|----------------|
| **Versiones** | 3 (Consola, Web, Notebook) |
| **Interfaz Web** | ⭐⭐⭐⭐⭐ Profesional con Streamlit |
| **Documentación** | ⭐⭐⭐⭐⭐ Exhaustiva y clara |
| **Código** | ⭐⭐⭐⭐⭐ Limpio y comentado |
| **Escalabilidad** | ⭐⭐⭐⭐ Preparado para crecer |
| **UX** | ⭐⭐⭐⭐⭐ Intuitiva y atractiva |

---

## 📞 Soporte

### Problemas Comunes

#### "No se encuentra el archivo CSV"
```bash
# Asegúrate de estar en la carpeta correcta
cd "Sprint 1"
# Verifica que existe el archivo
dir datos\tienda_aurelion.csv  # Windows
ls datos/tienda_aurelion.csv   # Linux/Mac
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

Para más ayuda, consulta la [documentación completa](Sprint%201/README.md).

---

## 📜 Licencia

Este proyecto es parte del programa educativo de IBM y está destinado únicamente para fines de aprendizaje.

---

## 🙏 Agradecimientos

- **IBM** por el programa de Inteligencia Artificial
- **Python Software Foundation** por Python
- **Streamlit** por el framework de aplicaciones web
- **Comunidad Open Source** por las herramientas utilizadas

---

<p align="center">
  <strong>⚔️ Tienda Aurelion - Donde la magia y la tecnología se encuentran ✨</strong>
</p>

<p align="center">
  Hecho con ❤️ para IBM - Inteligencia Artificial
</p>

---

**Última actualización:** Octubre 2025  
**Versión:** 1.0  
**Estado:** ✅ Completo

