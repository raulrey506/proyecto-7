import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos'

# Encabezado principal
st.header("visualizador de datos de venta de coches")

# Mostrar una vista previa de los datos
st.subheader("Vista previa del conjunto de datos")
st.write(car_data.head())

# Botón para mostrar el gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    fig = px.scatter(car_data, x="odometer", y="price", color="type",
                     title="Relación entre kilometraje y precio por tipo de vehículo",
                     labels={"odometer": "Kilometraje", "price": "Precio"})
    st.plotly_chart(fig)




