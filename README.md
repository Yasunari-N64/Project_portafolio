# Portafolio de Proyectos / Project Portfolio

![Estado del Proyecto](https://img.shields.io/badge/estado-activo-brightgreen.svg)
![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## Español

### Descripción
Bienvenidos a mi **portafolio de Analista de Datos**. Este repositorio reúne **10 proyectos reales** que demuestran dominio en **análisis exploratorio, pruebas estadísticas, machine learning, clustering y despliegue de aplicaciones web**.  

Desde la **optimización de campañas publicitarias** (ROMI, LTV, CAC), hasta el **desarrollo de dashboards interactivos** (Streamlit, Tableau) y la **identificación de operadores ineficaces mediante KMeans**, cada proyecto resuelve desafíos de negocio con **Python, pandas, scikit-learn, Seaborn, SciPy y más**.  

Incluye:  
- Análisis de embudos de ventas y experimentos A/A/B  
- Pruebas de hipótesis (t-Student, Mann-Whitney)  
- Visualización avanzada y storytelling con datos  
- Aplicación web desplegada [](https://project-portafolio.onrender.com)  

**Enfoque: impacto medible, decisiones basadas en datos, resultados accionables.**

Incluye:  
- Análisis de embudos de ventas y experimentos A/A/B  
- Pruebas de hipótesis (t-Student, Mann-Whitney)  
- Visualización avanzada y storytelling con datos  
- Aplicación web desplegada [](https://project-portafolio.onrender.com)  

**Enfoque: impacto medible, decisiones basadas en datos, resultados accionables.**

### Tabla de Contenidos
- [Tienda Comestibles Instacart](#tienda-comestibles-instacart)
- [Telecomunicaciones Megaline](#telecomunicaciones-megaline)
- [Ventas Videojuegos](#ventas-videojuegos)
- [Análisis de Mercado de Autos](#análisis-de-mercado-de-autos)
- [Análisis Retención de Clientes de Gimnasios](#análisis-retención-de-clientes-de-gimnasios)
- [Análisis de Tendencias de YouTube (Dashboard)](#análisis-de-tendencias-de-youtube-dashboard)
- [Experimento AAB para Aplicación de Empresa Alimenticia Emergente](#experimento-aab-para-aplicación-de-empresa-alimenticia-emergente)
- [Análisis de Negocio Showz](#análisis-de-negocio-showz)
- [Pruebas de Hipótesis de Marketing para Incrementar Ingresos](#pruebas-de-hipótesis-de-marketing-para-incrementar-ingresos)
- [**Identificación de Operadores Ineficaces en CallMeMaybe (Proyecto Intensivo)**](#identificación-de-operadores-ineficaces-en-callmemaybe-proyecto-intensivo)  
  *(Proyecto intensivo final – Clustering + Hipótesis + Recomendaciones de negocio)*
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

### Análisis Retención de Clientes de Gimnasios

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

### Análisis de Tendencias de YouTube (Dashboard)

**Descripción**: Como Analista de Vídeos Publicitarios en la agencia **Sterling & Draper** 📈, mi rol consiste en identificar tendencias en YouTube para orientar estrategias de marketing. Cada video pertenece a una categoría (entretenimiento, música, noticias y política, etc.), una región y una fecha de tendencia. Un video puede permanecer en tendencias varios días consecutivos.  

Semanalmente, las nuevas integrantes **Melanie** y **Ashok** requieren respuestas a:  
- ¿Qué categorías dominaron las tendencias la semana pasada?  
- ¿Cómo se distribuyeron geográficamente?  
- ¿Qué categorías destacaron en Estados Unidos?  

En mi sexta semana, automatice el proceso mediante un **dashboard interactivo** para agilizar el análisis y la toma de decisiones.

**Resultado**:  
Dashboard interactivo **“Análisis de Tendencias de Videos por Región y Categoría”**, con los siguientes componentes:  
- **Barra deslizante de fechas** 📅 para explorar períodos específicos.  
- **Filtro de región/país** 🌍 para análisis focalizado.  
- **Gráfica de áreas (absoluta)** 📈: evolución histórica de videos en tendencia.  
- **Gráfica de áreas (relativa)** 📉: tendencias normalizadas por región.  
- **Gráfica de pastel** 🥧: distribución porcentual de videos por país.  
- **Mapa de calor** 🔥: intensidad de tendencias por país y categoría.  

**Librerías y Herramientas**:  
![Tableau](https://img.shields.io/badge/tableau-%23E97627.svg?style=flat&logo=tableau&logoColor=white)

### Experimento AAB para Aplicación de Empresa Alimenticia Emergente

**Descripción**: Como Analista de Datos en una startup de productos alimenticios, analicé el comportamiento de usuarios en la app móvil. Estudié el **embudo de ventas** para identificar cuántos usuarios completan la compra y dónde se producen abandonos clave.  

Posteriormente, evalué un **experimento A/A/B** sobre un rediseño de fuentes:  
- **A1 y A2**: grupos de control con fuentes originales.  
- **B**: grupo de prueba con fuentes nuevas.  

El objetivo fue validar si el cambio afecta la experiencia del usuario. Los grupos A/A permiten verificar la consistencia estadística y detectar sesgos antes de comparar con B.

**Resultado**:  
No se encontraron diferencias significativas entre los grupos:  
- **A1**: 246 usuarios por evento clave  
- **A2**: 247 usuarios por evento clave  
- **B**: 248 usuarios por evento clave  

El cambio de fuentes **no impactó el comportamiento del usuario**. El experimento se considera **fallido**.

**Recomendación**:  
Mantener las fuentes actuales de la aplicación.

**Librerías**:  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)  
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)  
![Seaborn](https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6)  
![SciPy](https://img.shields.io/badge/scipy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white)

### Análisis de Negocio Showz

**Descripción**: Durante mis prácticas en el departamento de analítica de **Showz**, empresa líder en venta de entradas para eventos, optimicé los gastos de marketing mediante análisis de datos de 2017–2018. Conté con registros de visitas, pedidos y costos publicitarios.  

Investigué:  
- Comportamiento del usuario en la plataforma.  
- Tiempo entre registro y primera compra.  
- Valor del cliente a lo largo del tiempo (**LTV**).  
- Punto de recuperación del costo de adquisición (**CAC Payback**).  

**Pasos clave**:  
1. **Preprocesamiento**: carga y optimización de datos (`visits_log_us.csv`, `orders_log_us.csv`, `costs_us.csv`).  
2. **Métricas calculadas**:  
   - Uso diario, semanal y mensual (usuarios y sesiones).  
   - Duración promedio de sesión y frecuencia de retorno.  
   - Conversión por cohorte y canal de adquisición.  
   - Tamaño promedio de pedido y LTV.  
   - Costo total por fuente, CAC y **ROMI** (Return on Marketing Investment).  

**Resultado**:  
El negocio invirtió en 10 fuentes publicitarias. Solo las **fuentes 1 y 2** generaron retornos significativos (**49%** y **9%** de ROMI). Las **fuentes 3, 4 y 10** resultaron en pérdidas, con la **fuente 3** como la más crítica (**-61%**). El resultado neto fue una **pérdida de $77,000** por inversiones ineficientes.

**Recomendaciones**:  
- **Eliminar** fuentes 3, 4 y 10 (ROMI negativo).  
- **Concentrar** presupuesto en fuentes 1 y 2 (priorizando la 1).  
- **Reasignar** inversión de fuentes 5 y 9 hacia las más rentables.  
- **Monitorear** fuente 7 (orgánica con ingresos sin costo).  

**Librerías**:  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)  
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)  
![Seaborn](https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6)

### Pruebas de Hipótesis de Marketing para Incrementar Ingresos

**Descripción**: Como Analista de Datos en una gran tienda online, colaboré con el equipo de marketing para priorizar hipótesis de crecimiento y ejecutar un **test A/B** enfocado en aumentar ingresos.  

**Parte 1 – Priorización de Hipótesis**  
Utilicé los frameworks **ICE** y **RICE** para ordenar 9 hipótesis según su potencial (`Reach`, `Impact`, `Confidence`, `Effort`). RICE incorpora el alcance del público, modificando la prioridad frente a ICE.

**Parte 2 – Análisis del Test A/B**  
Con datos de pedidos (`orders_us.csv`) y visitas (`visits_us.csv`), realicé:  
- Gráficas de **ingreso acumulado**, **tamaño promedio de pedido** y **diferencia relativa** (B vs A).  
- Análisis de **tasa de conversión diaria** por grupo.  
- Distribución de pedidos por usuario y precios (gráficos de dispersión).  
- Cálculo de **percentiles 95 y 99** para detectar anomalías.  
- Pruebas de **significancia estadística** (Mann-Whitney U) en conversión y tamaño de pedido (datos crudos y filtrados).

**Resultado**:  
El **grupo B** (versión modificada) superó al **grupo A** con una **tasa de conversión del 3.02%**, un **+18%** respecto al grupo A. Aunque el tamaño promedio de pedido fue similar, el **ingreso acumulado** confirma mayor rentabilidad a largo plazo.  

**Conclusión**: **ÉXITO**. Se recomienda **detener la prueba e implementar la versión B**. Para aumentar el ticket promedio, evaluar nuevas hipótesis.

**Librerías**:  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)  
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)  
![Seaborn](https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6)  
![SciPy](https://img.shields.io/badge/scipy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white)

<div style="background: linear-gradient(135deg, #1e3a8a, #3b82f6); padding: 20px; border-radius: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.15); margin: 25px 0; color: white; font-family: 'Segoe UI', sans-serif;">
  <h3 style="color: #ffffff; margin-top: 0; text-align: center; font-size: 1.5em;">Identificación de Operadores Ineficaces en CallMeMaybe (Proyecto Intensivo)</h3>
  
  <p><strong>Descripción</strong>: En <strong>CallMeMaybe</strong>, servicio de telefonía virtual, desarrollé una función analítica para detectar operadores ineficaces. Un operador se considera ineficaz si presenta:<br>
  • <strong>Alta cantidad de llamadas perdidas</strong> (entrantes).<br>
  • <strong>Tiempo de espera prolongado</strong> (entrantes).<br>
  • <strong>Bajo volumen de llamadas salientes</strong> (si aplica).</p>

  <p><strong>Metodología</strong>:<br>
  1. <strong>Análisis exploratorio</strong>: carga, limpieza, enriquecimiento y visualización.<br>
  2. <strong>Clasificación</strong>: mediante <strong>KMeans</strong> y criterios visuales.<br>
  3. <strong>Hipótesis</strong>: comparación estadística entre grupos.</p>

  <p><strong>Resultado</strong>:<br>
  • <strong>3 operadores</strong> cumplen <strong>los 3 criterios</strong> (outliers en pérdidas y espera).<br>
  • <strong>29 operadores</strong> cumplen <strong>2 criterios</strong> (peores en métricas clave).</p>

  <p><strong>Conclusiones</strong>: Problema en <strong>gestión de llamadas entrantes</strong> (capacidad, enrutamiento o formación). Impacto: <strong>mala experiencia del cliente</strong>.</p>

  <p><strong>Recomendaciones – 3 criterios</strong>:<br>
  1. Reentrenamiento urgente.<br>
  2. Revisión de enrutamiento.<br>
  3. Reducción temporal de carga.<br>
  4. Monitoreo diario con alertas.</p>

  <p><strong>Recomendaciones – 2 criterios</strong>:<br>
  1. Capacitación intensiva.<br>
  2. Ajuste de distribución.<br>
  3. Seguimiento semanal.</p>

  <p><strong>Librerías</strong>:<br>
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black" alt="Matplotlib">
  <img src="https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6" alt="Seaborn">
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/scipy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white" alt="SciPy">
  </p>
</div>

### Contacto

- **Autor**: Ariel Yasunari Atenco Saucedo
- **GitHub**: Yasunari-N64 (https://github.com/Yasunari-N64)
- **Correo**: yasunari.atenco.u@gmail.com

## English

### Description
Welcome to my **Data Analyst Portfolio**. This repository features **10 real-world projects** showcasing expertise in **exploratory data analysis, statistical testing, machine learning, clustering, and web app deployment**.  

From **optimizing ad spend** (ROMI, LTV, CAC) to building **interactive dashboards** (Streamlit, Tableau) and **detecting underperforming operators via KMeans clustering**, every project tackles business challenges using **Python, pandas, scikit-learn, Seaborn, SciPy, and more**.  

Includes:  
- Sales funnel analysis & A/A/B experimentation  
- Hypothesis testing (t-test, Mann-Whitney)  
- Advanced visualization & data storytelling  
- Live web app [](https://project-portafolio.onrender.com)  

**Focus: measurable impact, data-driven decisions, actionable insights.**

Includes:  
- Sales funnel analysis & A/A/B experimentation  
- Hypothesis testing (t-test, Mann-Whitney)  
- Advanced visualization & data storytelling  
- Live web app [](https://project-portafolio.onrender.com)  

**Focus: measurable impact, data-driven decisions, actionable insights.**

### Table of Contents
- [Instacart Grocery Store](#instacart-grocery-store)
- [Megaline Telecommunications](#megaline-telecommunications)
- [Video Game Sales](#video-game-sales)
- [Car Market Analytics](#car-market-analytics)
- [Gym Customer Retention Analysis](#gym-customer-retention-analysis)
- [YouTube Trending Analysis (Dashboard)](#youtube-trending-analysis-dashboard)
- [A/A/B Experiment for Emerging Food Tech App](#a-a-b-experiment-for-emerging-food-tech-app)
- [Showz Business Analytics](#showz-business-analytics)
- [Marketing Hypothesis Testing to Boost Revenue](#marketing-hypothesis-testing-to-boost-revenue)
- [**Identifying Ineffective Operators at CallMeMaybe (Capstone Project)**](#identifying-ineffective-operators-at-callmemaybe-capstone-project)  
  *(Final intensive project – Clustering + Statistical Testing + Business Recommendations)*
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

### Gym Customer Retention Analysis

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

### YouTube Trending Analysis (Dashboard)

**Description**: As a **Video Advertising Analyst** at **Sterling & Draper** 📈, I analyze YouTube trends to guide marketing strategies. Each video is assigned a category (entertainment, music, news & politics, etc.), a region, and a trending date. Videos may remain trending for multiple consecutive days.  

Weekly, new team members **Melanie** and **Ashok** request:  
- Which categories trended last week?  
- How were they distributed across regions?  
- Which categories were particularly strong in the United States?  

In my sixth week, I automated the process by building an **interactive dashboard** to streamline insights and decision-making.

**Result**:  
Interactive dashboard titled **“Video Trending Analysis by Region and Category”**, featuring:  
- **Date range slider** 📅 for time-based exploration.  
- **Region/country filter** 🌍 for targeted analysis.  
- **Absolute area chart** 📈: historical trend volume over time.  
- **Relative area chart** 📉: normalized trends by region.  
- **Pie chart** 🥧: percentage distribution of trending videos by country.  
- **Heatmap** 🔥: trend intensity by country and category.  

**Tools & Libraries**:  
![Tableau](https://img.shields.io/badge/tableau-%23E97627.svg?style=flat&logo=tableau&logoColor=white)

### A/A/B Experiment for Emerging Food Tech App

**Description**: As a Data Analyst at a food product startup, I analyzed user behavior within the mobile app. I mapped the **sales funnel** to determine how many users reach the purchase stage and where drop-offs occur.  

I then conducted an **A/A/B test** to evaluate a font redesign:  
- **A1 & A2**: control groups with original fonts.  
- **B**: test group with new fonts.  

The goal was to assess whether the visual change impacts user experience. Dual control groups (A/A) ensure statistical reliability and help detect hidden biases before comparing with B.

**Result**:  
No significant differences were observed:  
- **A1**: 246 users per key event  
- **A2**: 247 users per key event  
- **B**: 248 users per key event  

The font change **had no meaningful impact** on user behavior. The experiment is deemed **unsuccessful**.

**Recommendation**:  
Retain the current app fonts.

**Libraries**:  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)  
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)  
![Seaborn](https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6)  
![SciPy](https://img.shields.io/badge/scipy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white)

### Showz Business Analytics

**Description**: As an analytics intern at **Showz**, a leading event ticketing platform, I optimized marketing spend using data from 2017–2018. I worked with server logs (visits), order records, and advertising costs.  

I analyzed:  
- User engagement patterns.  
- Time from registration to first purchase.  
- Customer lifetime value (**LTV**).  
- Break-even point for customer acquisition cost (**CAC Payback**).  

**Key Steps**:  
1. **Data Prep**: loaded and optimized datasets (`visits_log_us.csv`, `orders_log_us.csv`, `costs_us.csv`).  
2. **Metrics Computed**:  
   - Daily, weekly, monthly active users and sessions.  
   - Average session duration and return frequency.  
   - Cohort-based conversion and acquisition channel performance.  
   - Average order value and LTV.  
   - Total spend per source, CAC, and **ROMI** (Return on Marketing Investment).  

**Result**:  
Ten ad sources were used. Only **sources 1 and 2** delivered strong returns (**49%** and **9%** ROMI). **Sources 3, 4, and 10** generated losses, with **source 3** being the worst (**-61%**). Net result: a **$77,000 loss** due to inefficient channels.

**Recommendations**:  
- **Discontinue** sources 3, 4, and 10 (negative ROMI).  
- **Prioritize** investment in sources 1 and 2 (especially source 1).  
- **Reallocate** budget from sources 5 and 9 to top performers.  
- **Monitor** source 7 (organic traffic with revenue at zero cost).  

**Libraries**:  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)  
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)  
![Seaborn](https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6)

### Marketing Hypothesis Testing to Boost Revenue

**Description**: As a Data Analyst at a major online retailer, I partnered with the marketing team to prioritize revenue-growth hypotheses and run an **A/B test**.  

**Part 1 – Hypothesis Prioritization**  
Applied **ICE** and **RICE** frameworks to rank 9 hypotheses based on `Reach`, `Impact`, `Confidence`, and `Effort`. RICE includes audience reach, shifting priorities compared to ICE.

**Part 2 – A/B Test Analysis**  
Using order (`orders_us.csv`) and visit (`visits_us.csv`) data, I performed:  
- Cumulative **revenue**, **average order value**, and **relative difference** (B vs A) charts.  
- Daily **conversion rate** analysis per group.  
- Scatter plots of orders per user and order prices.  
- **95th and 99th percentiles** to define anomalies.  
- **Statistical significance** tests (Mann-Whitney U) on conversion and order size (raw and filtered data).

**Result**:  
**Group B** (modified version) outperformed **Group A** with a **3.02% conversion rate** — an **18% increase**. Despite similar average order values, **cumulative revenue** confirms long-term gains.  

**Conclusion**: **SUCCESS**. Recommend **stopping the test and rolling out Group B**. To increase AOV, explore new hypotheses.

**Libraries**:  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)  
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)  
![Seaborn](https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6)  
![SciPy](https://img.shields.io/badge/scipy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white)

<div style="background: linear-gradient(135deg, #1e3a8a, #3b82f6); padding: 20px; border-radius: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.15); margin: 25px 0; color: white; font-family: 'Segoe UI', sans-serif;">
  <h3 style="color: #ffffff; margin-top: 0; text-align: center; font-size: 1.5em;">Identifying Ineffective Operators at CallMeMaybe (Capstone Project)</h3>
  
  <p><strong>Description</strong>: At <strong>CallMeMaybe</strong>, I built an analytics tool to flag underperforming operators. An operator is ineffective if they show:<br>
  • <strong>High missed incoming calls</strong>.<br>
  • <strong>Long wait times</strong>.<br>
  • <strong>Low outgoing volume</strong> (when required).</p>

  <p><strong>Methodology</strong>:<br>
  1. <strong>Exploratory analysis</strong>: load, clean, enrich, visualize.<br>
  2. <strong>Classification</strong>: via <strong>KMeans</strong> and visual rules.<br>
  3. <strong>Hypothesis testing</strong>: top vs. bottom performers.</p>

  <p><strong>Result</strong>:<br>
  • <strong>3 operators</strong> met <strong>all 3 criteria</strong> (outliers in misses & wait).<br>
  • <strong>29 operators</strong> met <strong>2 criteria</strong> (worse across KPIs).</p>

  <p><strong>Insights</strong>: Core issue in <strong>inbound handling</strong> (capacity, routing, training). Risk: <strong>customer churn</strong>.</p>

  <p><strong>Action Plan – 3 Criteria</strong>:<br>
  1. Urgent retraining.<br>
  2. Review routing logic.<br>
  3. Reduce load temporarily.<br>
  4. Daily alerts.</p>

  <p><strong>Action Plan – 2 Criteria</strong>:<br>
  1. Intensive training.<br>
  2. Balance call distribution.<br>
  3. Weekly monitoring.</p>

  <p><strong>Libraries</strong>:<br>
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black" alt="Matplotlib">
  <img src="https://img.shields.io/badge/seaborn-%23ffffff.svg?style=flat&logo=python&logoColor=%23006BA6" alt="Seaborn">
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/scipy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white" alt="SciPy">
  </p>
</div>

### Contact

- **Author**: Ariel Yasunari Atenco Saucedo
- **GitHub**: Yasunari-N64 (https://github.com/Yasunari-N64)
- **Email**: yasunari.atenco.u@gmail.com
