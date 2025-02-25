import utilidades as util
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Proyecto de Streamlit', page_icon=':shark:', layout='wide', initial_sidebar_state='auto')    # Configuración de la página

#llamamos la funcion de utilidades

util.generarMenu()

# pagina de presentacion o index

# estructura de presentación

left_column, center_column, right_column = st.columns([1, 5, 1], vertical_alignment='center')

# edito la columna central
with center_column:
    st.title('informe de la liga colombiana 2024-2')
    st.write('Este es un proyecto para visualisar el rendimiento d elos equipos colombianos en la liga de futbol')
    st.write('Aquí se puede escribir una descripción del proyecto')
    imagen = Image.open('media/pngegg.png')
    st.image(imagen, width=400, caption='Vegetacion')  # Centrado y tamaño ajustado

util.grafica()
