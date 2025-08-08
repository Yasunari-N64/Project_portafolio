import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Dashboard de Vehículos Usados", layout="wide")

# Título y descripción
st.title("Dashboard Interactivo de Vehículos Usados")
st.markdown(
    "Explora datos de vehículos usados con filtros personalizados y visualizaciones interactivas.")

# Cargar datos


@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    # Manejo de datos faltantes
    df['model_year'] = df['model_year'].fillna(df['model_year'].median())
    df['odometer'] = df['odometer'].fillna(df['odometer'].median())
    df['cylinders'] = df['cylinders'].fillna(df['cylinders'].mode()[0])
    return df


df = load_data()

# Barra lateral con filtros
st.sidebar.header("Filtros de Búsqueda")

# Filtro: Tipo de vehículo
vehicle_types = sorted(df['type'].dropna().unique())
selected_types = st.sidebar.multiselect(
    "Tipo de Vehículo", vehicle_types, default=vehicle_types[:3])

# Filtro: Rango de precio
min_price, max_price = int(df['price'].min()), int(df['price'].max())
price_range = st.sidebar.slider(
    "Rango de Precio ($)", min_price, max_price, (min_price, max_price))

# Filtro: Rango de año del modelo
min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())
year_range = st.sidebar.slider(
    "Rango de Año del Modelo", min_year, max_year, (min_year, max_year))

# Filtro: Condición
conditions = sorted(df['condition'].dropna().unique())
selected_conditions = st.sidebar.multiselect(
    "Condición", conditions, default=conditions)

# Filtro: Tipo de combustible
fuels = sorted(df['fuel'].dropna().unique())
selected_fuels = st.sidebar.multiselect(
    "Tipo de Combustible", fuels, default=fuels)

# Filtro: Tracción 4x4
is_4wd = st.sidebar.checkbox("Solo vehículos 4x4", value=False)

# Filtro: Rango de kilometraje
min_odometer, max_odometer = int(
    df['odometer'].min()), int(df['odometer'].max())
odometer_range = st.sidebar.slider(
    "Rango de Kilometraje (millas)", min_odometer, max_odometer, (min_odometer, max_odometer))

# Filtrar datos
filtered_df = df[
    (df['type'].isin(selected_types)) &
    (df['price'].between(price_range[0], price_range[1])) &
    (df['model_year'].between(year_range[0], year_range[1])) &
    (df['condition'].isin(selected_conditions)) &
    (df['fuel'].isin(selected_fuels)) &
    (df['odometer'].between(odometer_range[0], odometer_range[1]))
]
if is_4wd:
    filtered_df = filtered_df[filtered_df['is_4wd'] == 1]

# Mostrar número de resultados
st.write(f"**Vehículos encontrados: {len(filtered_df)}**")

# Layout de gráficos
col1, col2 = st.columns(2)

# Gráfico 1: Histograma de Precios
with col1:
    st.subheader("Distribución de Precios")
    fig1 = px.histogram(filtered_df, x="price", nbins=30,
                        title="Distribución de Precios")
    fig1.update_layout(xaxis_title="Precio ($)", yaxis_title="Cantidad")
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Dispersión Precio vs. Kilometraje
with col2:
    st.subheader("Precio vs. Kilometraje")
    fig2 = px.scatter(filtered_df, x="odometer", y="price", color="type",
                      hover_data=["model", "model_year"], title="Precio vs. Kilometraje por Tipo")
    fig2.update_layout(xaxis_title="Kilometraje (millas)",
                       yaxis_title="Precio ($)")
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Precio Promedio por Tipo
with col1:
    st.subheader("Precio Promedio por Tipo de Vehículo")
    avg_price_by_type = filtered_df.groupby(
        "type")["price"].mean().reset_index()
    fig3 = px.bar(avg_price_by_type, x="type", y="price",
                  title="Precio Promedio por Tipo")
    fig3.update_layout(xaxis_title="Tipo de Vehículo",
                       yaxis_title="Precio Promedio ($)")
    st.plotly_chart(fig3, use_container_width=True)

# Gráfico 4: Box Plot de Precios por Condición
with col2:
    st.subheader("Distribución de Precios por Condición")
    fig4 = px.box(filtered_df, x="condition", y="price",
                  title="Precios por Condición")
    fig4.update_layout(xaxis_title="Condición", yaxis_title="Precio ($)")
    st.plotly_chart(fig4, use_container_width=True)

# Tabla de datos filtrados
st.subheader("Datos Filtrados")
st.dataframe(filtered_df[["model", "model_year", "price", "odometer",
             "type", "condition", "fuel"]], use_container_width=True)

# Opción para descargar datos filtrados
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Descargar Datos Filtrados (CSV)", csv,
                   "filtered_vehicles.csv", "text/csv")
