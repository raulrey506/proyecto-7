import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos (asegúrate de tener el archivo en la ruta correcta)
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la app
st.title("Visualizador de Datos de Vehículos Usados")

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar una vista previa del DataFrame
st.subheader("Vista previa del conjunto de datos")
st.write(car_data.head())

# Botón para mostrar gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    fig = px.scatter(car_data, x="odometer", y="price", color="type",
                     title="Relación entre kilometraje y precio por tipo de vehículo",
                     labels={"odometer": "Kilometraje", "price": "Precio"})
    st.plotly_chart(fig)

# Casilla de verificación para mostrar el histograma
if st.checkbox("Mostrar histogramas de modelos con más de 1000 anuncios"):
    # Contar modelos
    model_counts = car_data['model'].value_counts()
    top_models = model_counts[model_counts > 1000].reset_index()
    top_models.columns = ['model', 'count']

    fig_hist = px.bar(top_models, x='model', y='count',
                      title='Modelos con más de 1000 anuncios',
                      labels={'model': 'Modelo', 'count': 'Cantidad de anuncios'})
    st.plotly_chart(fig_hist)

