# Portafolio de Proyectos / Project Portfolio

![Estado del Proyecto](https://img.shields.io/badge/estado-activo-brightgreen.svg)
![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## Español

### Descripción

Bienvenidos a mi portafolio de proyectos, donde muestro mis habilidades en análisis de datos, visualización y desarrollo de aplicaciones, adquiridas durante el bootcamp de Analista de Datos de TripleTen. Este repositorio incluye proyectos que abarcan desde exploración y limpieza de datos hasta análisis estadístico, visualización interactiva y despliegue de aplicaciones web. Cada proyecto utiliza herramientas modernas como Python, GitHub, Streamlit y Power BI, con un enfoque en resolver problemas reales de negocio.

### Tabla de Contenidos

- [Tienda Comestibles Instacart](#tienda-comestibles-instacart)
- [Telecomunicaciones Megaline](#telecomunicaciones-megaline)
- [Ventas Videojuegos](#ventas-videojuegos)
- [Análisis de Mercado de Autos](#car-market-analytics)
- [Análisis Retención de Clientes de Gimnasios](#análisis-retención-de-clientes-de-gimnasios)
- [Contacto](#contacto)

### Tienda Comestibles Instacart

**Descripción**: Este proyecto analiza el comportamiento de compra de los clientes de *Instacart*, una tienda en línea de comestibles. Se aplicaron habilidades de exploración, limpieza y manipulación de datos en diferentes *dataframes*, seguidas de visualizaciones significativas para identificar patrones. Se convirtieron archivos `.csv` en *dataframes*, se exploraron con métodos de *pandas* como `.info()` y `.head()`, y se transformaron los tipos de datos según la información de cada columna. Se identificaron y gestionaron datos duplicados y ausentes, correlacionando los *dataframes* mediante claves como `id` y `product_id`. Las visualizaciones (gráficas de barras e histogramas) revelaron patrones en los productos más comprados, la frecuencia de compra y el orden de los pedidos. **Resultado**: Los plátanos son los productos más populares por un amplio margen. ¿Será que los clientes no son humanos, sino monos o chimpancés? 😂🐒

**Librerías**:
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%23007ACC.svg?style=flat&logo=matplotlib&logoColor=white)

### Telecomunicaciones Megaline

**Descripción**: Este proyecto analiza los ingresos generados por las tarifas de un operador de telecomunicaciones, *Megaline*, para informar al departamento de publicidad. Se reforzaron habilidades de exploración y limpieza de datos, y se aplicaron pruebas estadísticas como *Levene* y *t-student* para comprobar hipótesis. Se exploraron archivos `.csv` convertidos en *dataframes*, se limpiaron y correlacionaron, y se visualizaron los datos con gráficas de barras, histogramas, diagramas de cajas y distribuciones normales. **Resultado**: Las pruebas estadísticas confirmaron que los ingresos promedio difieren entre planes, siendo el plan básico el que genera más ingresos. 📱

**Librerías**:
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%23007ACC.svg?style=flat&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/seaborn-%23007ACC.svg?style=flat&logo=seaborn&logoColor=white)
![SciPy](https://img.shields.io/badge/scipy-%23007ACC.svg?style=flat&logo=scipy&logoColor=white)

### Ventas Videojuegos

**Descripción**: Este proyecto analiza las ventas históricas de una tienda de videojuegos desde los años 80 hasta 2016, con el objetivo de realizar una prospectiva para 2017. Es un proyecto integrado que combina importación de librerías, exploración y limpieza de datos, visualización y pruebas de hipótesis. Se convirtió un archivo `.csv` en un *dataframe*, se limpiaron datos (tipos, duplicados, ausentes), y se enriquecieron con columnas de "ventas totales" y "generación". Las visualizaciones incluyeron gráficas de barras, líneas, dispersión y cajas, agrupando datos por consolas (top 5 en ventas). **Resultado**: Para 2017, se recomendó enfocarse en juegos de acción y deportes para plataformas de [Sony](https://www.sony.com/) 🎮, [Nintendo](https://www.nintendo.com/) 🎮 y [Microsoft](https://www.xbox.com/) 🎮, por ser los más rentables.

**Librerías**:
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%23007ACC.svg?style=flat&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/seaborn-%23007ACC.svg?style=flat&logo=seaborn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)

### Análisis de Mercado de Autos

**Descripción**: Este proyecto desarrolla un *dashboard* interactivo para una agencia de venta de autos usados, permitiendo a los clientes visualizar información de los vehículos disponibles. Se utilizaron herramientas de software como *GitHub* para versionamiento, *Visual Studio Code* para desarrollo, *Streamlit* para pruebas y *Render.com* para despliegue web ([ver aplicación](https://project-portafolio.onrender.com)). Se realizó una exploración y limpieza inicial de los datos, seguidas de la creación de un *dashboard* con un menú desplegable para seleccionar visualizaciones (gráficas de barras y dispersión) basadas en variables como precio, kilometraje, año modelo y condición. **Resultado**: Una aplicación funcional desplegada en línea, con visualizaciones interactivas. 🚗

**Librerías**:
![Streamlit](https://img.shields.io/badge/streamlit-%23FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/plotly-%233F4F75.svg?style=flat&logo=plotly&logoColor=white)

### Análisis Retención de Clientes de Gimnasios 🏋️‍♂️

**Descripción**: Este proyecto me posiciona como Analista de Datos para la “Cadena de Gimnasios Model Fitness” 💪, con el objetivo de diseñar una estrategia de interacción con clientes basada en datos analíticos. Los pasos realizados fueron:  
1. **Análisis Exploratorio de Datos (EDA)** 📊:  
   - Limpieza de datos 🧹.  
   - Visualización de los datos 📈.  
2. **Construcción de un Modelo de Aprendizaje Automático** 🤖, para predecir la cancelación de usuarios:  
   - `LogisticRegression`  
   - `RandomForestClassifier`  
3. **Agrupamiento de usuarios** en clusters con características similares 👥:  
   - `StandardScaler`  
   - `scaler.fit_transform`  
4. **Interpretación de clusters** y recomendaciones estratégicas 📋.  

**Resultado**: Se propusieron las siguientes estrategias:  
1. Fomentar contratos de mayor duración para aumentar la retención 📅.  
2. Dirigirse a clientes con alta propensión a abandonar mediante estrategias de *engagement* 🎯.  
3. Atraer y retener a usuarios de 30 años en adelante con programas personalizados 🎂.  
4. Personalizar la experiencia para clientes que viven lejos del gimnasio 🚗.

**Librerías**:
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6)
![SciPy](https://img.shields.io/badge/scipy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white)

### Contacto

- **Autor**: Ariel Yasunari Atenco Saucedo
- **GitHub**: Yasunari-N64 (https://github.com/Yasunari-N64)
- **Correo**: yasunari.atenco.u@gmail.com

## English

### Description

Welcome to my project portfolio, showcasing my skills in data analysis, visualization, and application development, acquired during the TripleTen Data Analyst Bootcamp. This repository includes projects ranging from data exploration and cleaning to statistical analysis, interactive visualization, and web application deployment. Each project leverages modern tools like Python, GitHub, Streamlit, and Power BI, focusing on solving real-world business problems.

### Table of Contents

- [Instacart Grocery Store](#instacart-grocery-store)
- [Megaline Telecommunications](#megaline-telecommunications)
- [Video Game Sales](#video-game-sales)
- [Car Market Analytics](#car-market-analytics)
- [Gym Customer Retention Analysis](#gym-customer-retention-analysis)
- [Contact](#contact)

### Instacart Grocery Store

**Description**: This project analyzes customer purchasing behavior at *Instacart*, an online grocery store. It involves data exploration, cleaning, and manipulation across multiple *dataframes*, followed by meaningful visualizations to identify patterns. CSV files were converted into *dataframes*, explored using *pandas* methods like `.info()` and `.head()`, and data types were adjusted based on column content. Duplicates and missing data were handled, and *dataframes* were correlated using keys like `id` and `product_id`. Visualizations (bar charts and histograms) revealed patterns in the most purchased products, purchase frequency, and order sequence. **Result**: Bananas are the most popular product by a wide margin. Are the customers human, or perhaps monkeys or chimpanzees? 😂🐒

**Libraries**:
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%23007ACC.svg?style=flat&logo=matplotlib&logoColor=white)

### Megaline Telecommunications

**Description**: This project analyzes revenue generated by *Megaline*'s tariffs to inform the advertising department. It reinforced data exploration and cleaning skills and introduced statistical tests like *Levene* and *t-student* for hypothesis testing. CSV files were converted into *dataframes*, cleaned, and correlated, with visualizations including bar charts, histograms, box plots, and normal distributions. **Result**: Statistical tests confirmed that average revenues differ between plans, with the basic plan generating the most revenue. 📱

**Libraries**:
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%23007ACC.svg?style=flat&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/seaborn-%23007ACC.svg?style=flat&logo=seaborn&logoColor=white)
![SciPy](https://img.shields.io/badge/scipy-%23007ACC.svg?style=flat&logo=scipy&logoColor=white)

### Video Game Sales

**Description**: This project analyzes historical sales data from a video game store from the 1980s to 2016, aiming to forecast trends for 2017. It integrates skills in library imports, data exploration, cleaning, visualization, and hypothesis testing. A CSV file was converted into a *dataframe*, cleaned (types, duplicates, missing data), and enriched with "total sales" and "generation" columns. Visualizations included bar, line, scatter, and box plots, grouping data by consoles (top 5 in sales). **Result**: For 2017, the recommendation was to focus on action and sports games for [Sony](https://www.sony.com/) 🎮, [Nintendo](https://www.nintendo.com/) 🎮, and [Microsoft](https://www.xbox.com/) 🎮 platforms, as they are the most profitable.

**Libraries**:
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%23007ACC.svg?style=flat&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/seaborn-%23007ACC.svg?style=flat&logo=seaborn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)

### Car Market Analytics

**Description**: This project develops an interactive *dashboard* for a used car sales agency, allowing clients to visualize available vehicle data. It used software tools like *GitHub* for version control, *Visual Studio Code* for development, *Streamlit* for testing, and *Render.com* for web deployment ([view application](https://project-portafolio.onrender.com)). Initial data exploration and cleaning were followed by creating a *dashboard* with a dropdown menu for selecting visualizations (bar and scatter plots) based on variables like price, mileage, model year, and condition. **Result**: A functional web application with interactive visualizations. 🚗

**Libraries**:
![Streamlit](https://img.shields.io/badge/streamlit-%23FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/plotly-%233F4F75.svg?style=flat&logo=plotly&logoColor=white)

### Gym Customer Retention Analysis 🏋️‍♂️

**Description**: In this project, I took on the role of a Data Analyst for the “Model Fitness Gym Chain” 💪, with the goal of designing a customer engagement strategy based on data analytics. The steps performed were:  
1. **Exploratory Data Analysis (EDA)** 📊:  
   - Data cleaning 🧹.  
   - Data visualization 📈.  
2. **Building a Machine Learning Model** 🤖 to predict user churn:  
   - `LogisticRegression`  
   - `RandomForestClassifier`  
3. **User clustering** into groups with similar characteristics 👥:  
   - `StandardScaler`  
   - `scaler.fit_transform`  
4. **Cluster interpretation** and strategic recommendations 📋.  

**Result**: The following strategies were proposed:  
1. Promote longer-term contracts to increase retention 📅.  
2. Target customers with high churn propensity through *engagement* strategies 🎯.  
3. Attract and retain users aged 30 and older with personalized programs 🎂.  
4. Customize the experience for customers who live far from the gym 🚗.
   
**Libraries**:
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6)
![SciPy](https://img.shields.io/badge/scipy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white)

### Contact

- **Author**: Ariel Yasunari Atenco Saucedo
- **GitHub**: Yasunari-N64 (https://github.com/Yasunari-N64)
- **Email**: yasunari.atenco.u@gmail.com
