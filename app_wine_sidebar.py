# Importamos librerías necesarias
import streamlit as st
from PIL import Image
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="CatemosVino", page_icon="🍷", layout="wide")

# Barra lateral para la navegación
pagina = st.sidebar.selectbox("Navegación", ["Inicio", "Quiénes Somos", "Qué Ofrecemos", "Nuestros Vinos"])

# Función para cargar y redimensionar el logo
def cargar_logo(ruta, width=250):
    try:
        logo = Image.open(ruta)
        aspect_ratio = logo.height / logo.width
        height = int(width * aspect_ratio)
        logo = logo.resize((width, height))
        return logo
    except FileNotFoundError:
        st.warning("⚠️ No se encontró el archivo del logo.")
        return None

# Mostrar contenido según la página seleccionada
if pagina == "Inicio":
    # Cargar y mostrar el logo con tamaño reducido
    logo = cargar_logo("data/img/logo_catemosvino.png", width=500)
    if logo:
        st.image(logo, use_container_width=False)

    # Encabezado de la página
    st.title("Bienvenidos a CatemosVino 🍷")
    st.markdown("### Explorando el mundo del vino con pasión y calidad.")

    # Sección de categorías de vinos
    st.subheader("Nuestros tipos de vinos")
    col1, col2, col3, col4 = st.columns(4)

    # Lista de vinos con iconos
    categorias_vinos = {
        "Vino Blanco": "data/img/vino_blanco.png",
        "Vino Tinto": "data/img/vino_tinto.png",
        "Vino Rosado": "data/img/vino_rosado.png",
        "Cava / Espumoso": "data/img/vino_cava.png"
    }

    # Mostrar iconos en columnas con imágenes redimensionadas
    def cargar_icono(ruta, width=80):
        try:
            icono = Image.open(ruta)
            aspect_ratio = icono.height / icono.width
            height = int(width * aspect_ratio)  # Mantiene la proporción
            icono = icono.resize((width, height))
            return icono
        except FileNotFoundError:
            return None

    for col, (nombre, icono) in zip([col1, col2, col3, col4], categorias_vinos.items()):
        img = cargar_icono(icono)
        if img:
            col.image(img)
        else:
            col.warning(f"⚠️ No se encontró el icono para {nombre}")

        col.markdown(f"**{nombre}**")

elif pagina == "Quiénes Somos":
    st.title("Quiénes Somos")
    st.markdown("""
## 🍷 CatemosVino: La excelencia del vino español en el mundo

Bienvenidos a **CatemosVino**, una empresa española especializada en la **exportación de vinos con Denominación de Origen (D.O.)** a nivel internacional.  
Nuestra misión es conectar las mejores bodegas de España con distribuidores, importadores y amantes del vino en todo el mundo, garantizando calidad, autenticidad y una experiencia única en cada botella.

---

### 🌍 **Nuestra misión**
En **CatemosVino**, trabajamos para que el mundo descubra la riqueza vinícola de España, exportando vinos que reflejan la tradición y la innovación de nuestras bodegas.  
Nos enfocamos en ofrecer:
- **Vinos con Denominación de Origen (D.O.)**, certificados por su calidad y autenticidad.
- **Un servicio ágil y personalizado**, adaptado a las necesidades de cada mercado.
- **Asesoramiento experto**, con un equipo comercial altamente capacitado.

---

### 🍇 **Nuestra selección de vinos**
Trabajamos con una exclusiva selección de bodegas en las principales regiones vinícolas de España, ofreciendo vinos que representan la diversidad de nuestro país:

✅ **Vinos Tintos**: Potentes, elegantes y con carácter, provenientes de regiones como **Ribera del Duero, Rioja y Priorat**.  
✅ **Vinos Blancos**: Frescos y expresivos, destacando los **Albariños de Rías Baixas y Verdejos de Rueda**.  
✅ **Vinos Rosados**: Aromáticos y vibrantes, ideales para cualquier ocasión.  
✅ **Cavas y Espumosos**: La mejor expresión del método tradicional en **Cataluña y otras regiones**.  

---

### 💼 **Apoyo a nuestra red comercial**
Sabemos que el éxito de nuestros clientes y comerciales es clave, por eso ofrecemos:
            
✔ **Material de ventas y formación**, incluyendo fichas técnicas y argumentarios de producto.  
✔ **Gestión eficiente de pedidos y logística internacional**, asegurando entregas a tiempo.  
✔ **Soporte en ferias y eventos internacionales**, para fortalecer la presencia de nuestros vinos en mercados clave.  

📌 *Si necesitas más información o materiales de apoyo, no dudes en contactarnos.*  

---

### 📞 **Contáctanos**
📍 **Sede:** Madrid, España  
📧 **Email:** contacto@catemosvino.com  
🌎 **Exportamos a más de 30 países**  
""")
    
elif pagina == "Qué Ofrecemos":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        logo = cargar_logo("data/img/mundo.png", width=500)
        if logo:
            st.image(logo, use_container_width=False)
    st.title("Qué Ofrecemos")
    st.markdown("""
                En **CatemosVino** nos apasiona el mundo del vino y por ello ofrecemos una selecta gama de vinos españoles de alta calidad, procedentes de bodegas dirigidas por productores y enólogos comprometidos con la excelencia. Nuestro catálogo está cuidadosamente elaborado, incluyendo proyectos de pequeña y mediana escala, así como vinos de edición limitada, donde cada etiqueta refleja la esencia de una tierra, la dedicación de familias y un arraigo que se transmite en cada sorbo.

    Asimismo, en **CatemosVino** seleccionamos y comercializamos vinos que destacan por su excelente relación calidad/precio, fundamentados en nuestro profundo conocimiento de los productores y en una constante actualización respecto a las necesidades y tendencias del mercado. Nuestra colaboración con un grupo de bodegas profesionales nos permite ofrecer un porfolio atractivo y completo, complementando nuestra oferta con vinos que se adaptan a diferentes gustos y ocasiones.

    El reconocimiento y la valoración de nuestros clientes son la mejor muestra de nuestro compromiso con la calidad y la pasión por el vino español. En **CatemosVino**, trabajamos día a día para brindarte una experiencia única, donde la tradición se une con la innovación, y cada botella cuenta una historia singular.
    """
)
    
elif pagina == "Nuestros Vinos":
    # Cargar el DataFrame con datos simulados
    df = pd.read_csv('data/webs_vinos.csv')

    # Título de la aplicación
    st.title("Nuestro Vinos D.O.")

    # Dividir en bloques de 34 filas
    num_filas = 34
    num_columnas = 3
    chunks = [df.iloc[i:i+num_filas] for i in range(0, len(df), num_filas)]

    # Mostrar la tabla con tres columnas
    for chunk in chunks:
        cols = st.columns(num_columnas)  # Crear tres columnas

        for i, (idx, row) in enumerate(chunk.iterrows()):
            col = cols[i % num_columnas]  # Seleccionar columna según el índice

            with col:
                st.markdown(
                    f"""
                    <a href="{row['Web']}" target="_blank">
                    <img src="{row['Imagen']}" alt="{row['Nombre']}" title="{row['Nombre']}" style="width: 100%; max-width: 170px; height: auto; display: block; margin: auto;">
                    </a>
                    """, unsafe_allow_html=True
                )
                #st.image(row["Imagen"], width=170)
                #st.write(f"**{row['Nombre']}** [ Web]({row['Web']})")
                st.markdown("---")

# Pie de página
st.markdown("---")
st.markdown("📌 *CatemosVino - Exportación de vinos de calidad.*")