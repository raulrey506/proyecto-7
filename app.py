import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos'

# Encabezado principal
st.header("Bienvenido a mi aplicación web")


hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
     fig = px.histogram(car_data, x="odometer")
     
     # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

# Botón 1 - Muestra un texto
if st.button("Haz clic para mostrar un mensaje"):
    st.write("¡Hola! Este es un mensaje de prueba.")

# Botón 2 - Muestra un gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    # Creamos un DataFrame de ejemplo
    df = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 15, 13, 17, 20],
        'categoría': ['A', 'B', 'A', 'B', 'A']
    })

    # Gráfico de dispersión con Plotly Express
    fig = px.scatter(df, x='x', y='y', color='categoría', title='Gráfico de dispersión ejemplo')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

import streamlit as st

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')






