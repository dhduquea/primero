import pandas as pd
import streamlit as st
import utilidades as util
from PIL import Image
import seaborn as sb


#visualizacion de datos
util.generarMenu()

st.title('datos de la liga colombiana 2024')
ruta = 'data/limpiezatorneo.csv'
df = pd.read_csv(ruta)

# configuramos la visualización
tex = 'cantidad de goles marcados por cada equipo'

util.informe(df, tex)  # Llamado a la función de utilidades