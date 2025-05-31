# proyecto-7

# Visualizador de Datos de Vehículos Usados

Este es un proyecto de aplicación web interactiva desarrollado con **Streamlit**. Visualiza datos de ventas de coches en EE. UU., permite explorar relaciones entre precio, kilometraje y tipo de vehículo, y muestra qué modelos son más populares.

## Características

- Carga de datos desde un archivo CSV (`vehicles_us.csv`)
- Gráfico de dispersión interactivo entre `odometer` y `price`
- Histograma de modelos de coche con más de 1000 anuncios
- Interfaz sencilla, desplegable con botones y casillas de verificación

## Requisitos

Instala las dependencias necesarias con conda:

```bash
conda install pandas
conda install -c plotly plotly
conda install -c conda-forge streamlit


Estructura del proyecto

proyecto-7/
│
├── app.py               # Código de la aplicación Streamlit
├── vehicles_us.csv      # Dataset de vehículos usados
└── README.md            # Este archivo

Cómo ejecutar:
Desde la terminal, navega al directorio del proyecto y ejecuta:
streamlit run app.py



Visualizaciones
Gráfico de dispersión: Muestra la relación entre el kilometraje (odometer) y el precio (price), segmentado por tipo de vehículo.

Histograma: Muestra qué modelos tienen más de 1000 anuncios en el dataset.

Créditos
Proyecto desarrollado como parte del curso de análisis de datos con Python y Streamlit.
📊 Desarrollado por Raúl claudio reyna
