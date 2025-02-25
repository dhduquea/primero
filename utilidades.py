import pandas as pd
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt
import seaborn as sns

def generarMenu():
    with st.sidebar:
        imagen = Image.open('media/pngegg.png')
        st.image(imagen,width=100, use_container_width=True)  # Centrado y tamaño ajustado
        st.page_link('app.py', label='Inicio')
        st.page_link('pages/informe.py', label='Visualización de datos')

        

def grafica():
    df = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 30, 40, 50]
    })
    fig, ax = plt.subplots()
    ax.plot(df['x'], df['y'])
    st.pyplot(fig)

def informe(df, titulo):
    df2 = pd.DataFrame(df)
    col1, col2, col3 = st.columns([1, 5, 1],
                                  vertical_alignment='center')
    with col2:
        st.markdown(titulo)
        df2.set_index('Local', inplace=True)
        st.write(df2, unsafe_allow_html=False)
        st.markdown('grafico')

        sns.set_style('whitegrid')
        total = df2.groupby('Local')[['goles local', 'goles visitate']].sum()
        goles = pd.DataFrame(total)
        goles['goles totales'] = goles['goles local'] + goles['goles visitate']
        goles = goles.reset_index()

        resultado = goles.groupby(['Local']).sum()
        resultado.plot(kind='bar', figsize=(10,10))
        plt.tight_layout()
        st.pyplot(plt)
