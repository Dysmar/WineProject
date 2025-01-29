# IMPORTAMOS LAS LIBRERIAS QUE QUEREMOS USAR
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
warnings.filterwarnings('ignore')
#st.set_option('deprecation.showPyplotGlobalUse', False)

# CONFIGURACION DE LA PAGINA
#CONFIGURACION DE LA PAGINA
st.set_page_config(
    page_title="Ayuntamiento de Barcelona",
    page_icon="r'data/webimg/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded", #opciones: collapsed, expanded NO OBLIGATORIO
)