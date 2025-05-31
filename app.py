import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la app
st.title("Visualizador de Datos de Vehículos Usados")

# Cargar los datos (asegúrate de tener el archivo en la ruta correcta)
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar una vista previa
st.subheader("Vista previa del conjunto de datos")
st.write(car_data.head())

# Botón para gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    fig = px.scatter(car_data, x="odometer", y="price", color="type",
                     title="Relación entre kilometraje y precio por tipo de vehículo",
                     labels={"odometer": "Kilometraje", "price": "Precio"})
    st.plotly_chart(fig)

mostrar_histograma = st.checkbox("Mostrar histograma de anuncios por marca")

if mostrar_histograma:
    marca_counts = car_data['manufacturer'].value_counts().reset_index()
    marca_counts.columns = ['manufacturer', 'count']

    fig_hist = px.bar(marca_counts, x='manufacturer', y='count',
                      title="Cantidad de anuncios por marca de coche",
                      labels={'manufacturer': 'Marca', 'count': 'Número de anuncios'})
    st.plotly_chart(fig_hist)

