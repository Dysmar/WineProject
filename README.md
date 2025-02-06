# CatamosVino - Análisis y Predicción del Mercado Vinícola

## Descripción del Proyecto
CatamosVino es una solución analítica diseñada para optimizar la comercialización del vino español en mercados nacionales e internacionales. Utilizando herramientas de análisis de datos, inteligencia de negocios y modelos predictivos, este proyecto proporciona información estratégica basada en datos para mejorar la toma de decisiones en el sector vinícola.

## Objetivo
El objetivo principal de este proyecto es el desarrollo de una API llamada **"CatamosVino"**, que integra datos de diversas fuentes oficiales y proporciona insights clave sobre la evolución del mercado vinícola.

## Funcionalidades Principales
- **Integración de Datos:** Incorporación de información de la Organización Internacional de la Viña y el Vino (OIV) y del Instituto de Viticultores de España (INFOVI).
- **Análisis Exploratorio de Datos (EDA):** Uso de Python para descubrir patrones y tendencias clave en el mercado vinícola.
- **Visualización Interactiva en Power BI:** Dashboards dinámicos para evaluar la comercialización de las Denominaciones de Origen Protegidas (DOPs).
- **Modelos Predictivos en Azure Machine Learning:** Implementación de algoritmos de Machine Learning para prever la evolución de la demanda y mejorar la estrategia de ventas.
- **Interfaz Web con Streamlit:** Plataforma web para la visualización de datos y consulta de información de manera accesible e interactiva.

## Estructura del Repositorio
```
CatamosVino/                  # Aplicación web en Streamlit
│-- data/                    # Archivos de datos crudos y procesados
│-- EDA/               # Jupyter Notebooks para análisis EDA y Machine Learning
│-- PowerBI/              # Dashboards desarrollados en Power BI
│-- ML/                     # Código de la API "CatamosVino"
│-- README.md                # Documentación principal del repositorio


## Requisitos
Para ejecutar este proyecto, se necesitan las siguientes herramientas y librerías:
- Python 3.8+
- Pandas, NumPy, Matplotlib, Seaborn (para EDA)
- Power BI (para visualización interactiva)
- Azure Machine Learning SDK (para modelos predictivos)
- Streamlit (para la interfaz web)
- FastAPI (para la implementación de la API)

## Instalación y Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/CatamosVino.git
   cd CatamosVino
   ```
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la aplicación web en Streamlit:
   ```bash
   streamlit run web_app/app.py
   ```
4. Para iniciar la API con FastAPI:
   ```bash
   uvicorn api.main:app --reload
   ```

## Equipo de Desarrollo
- **Expositor 1:** Introducción y presentación del proyecto, integración de Streamlit.
- **Expositor 2:** Análisis exploratorio de datos (EDA) con Python.
- **Expositor 3:** Evaluación del mercado con visualización en Power BI.
- **Expositor 4:** Creación y despliegue de modelos predictivos en Azure Machine Learning.

## Análisis de Datos

Para realizar el EDA, se han utilizado los siguientes archivos CSV:
- `exportacion_spain_DOP.csv`
- `exportacion_spain.csv`
- `dataVino2023.csv`
- `dfvino_unido.csv`

### **Jupyter Notebooks Utilizados**

#### **EDA_OIV_definitivo.ipynb**
- Importación de datos y librerías.
- Exploración de la estructura de datos.
- Análisis de valores atípicos con Boxplot.
- Correlación de variables y visualizaciones con `sns.heatmap` y `sns.scatterplot`.
- Análisis de tendencias en la exportación por países con `sns.lineplot`.

#### **EDA_export_definitivo.ipynb**
- Importación y exploración de `df_expor_dop`.
- Transformación de datos con `melt()`.
- Creación de visualizaciones en `sns.barplot` y `sns.heatmap`.
- Generación de reportes en CSV con `to_csv()`.

#### **Union_de_China.ipynb**
- Unificación de variables clave mediante `pd.concat()`.
- Validación de la unificación con `shape`, `head()`, `unique()`.
- Creación del archivo final `dfvino_unido.csv`.

## Creación de una API Predictiva con Machine Learning en Azure

Se ha desarrollado una API en Azure Machine Learning para optimizar la comercialización internacional del vino DOP. La API estima el precio de exportación considerando país destino, hábitos de consumo y características de la DOP.

### **Pasos Clave en el Desarrollo**
1. **Diseño e Implementación del Modelo**
   - Normalización de variables continuas.
   - División del dataset (80% entrenamiento, 20% testeo).
   - Evaluación de algoritmos de regresión y clasificación.

2. **Optimización con AutoML**
   - Selección automática del mejor modelo.
   - Uso de `VotingEnsemble` para mejorar la precisión.
   - Exposición de la API a través de un endpoint en Azure.

3. **Desarrollo de una Herramienta de Selección de DOP**
   - Creación de un modelo adicional para recomendar la DOP más adecuada.
   - Implementación de `ExtremeRandomTrees` con una exactitud del 80%.

4. **Beneficios de la API Predictiva**
   - Optimiza la fijación de precios.
   - Identifica oportunidades de exportación.
   - Automatiza la toma de decisiones comerciales.

---
**CatamosVino** representa una herramienta innovadora para la industria vinícola, combinando datos, tecnología y análisis predictivo para potenciar la comercialización del vino español en mercados globales.

