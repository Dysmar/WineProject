# Importamos librerías necesarias
import streamlit as st
from PIL import Image
import pandas as pd
import json
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Configuración de la página
st.set_page_config(page_title="CatemosVino", page_icon="🍷", layout="wide")

# Navegación por pestañas
tabs = ["Inicio", "Quiénes Somos", "Qué Ofrecemos", "Ferias", "Nuestros Vinos", "EDA", "PowerBI", "ML"]
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(tabs)

with tab1:
    image_logob = 'https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/logo_catemosvino.png'
    st.markdown(
        f"""
        <style>
        .image-container {{
            position: relative;
            display: inline-block;
            width: 100%;
            text-align: center;
        }}
        .image-container img {{
            width: 100%;
            height: auto;
            display: block;
            border-radius: 10px;
        }}

        </style>
        <div class="image-container">
            <img src="{image_logob}" alt="WWB: Feria de Vino" title="CatemosVino Banner">
        </div>
        """, unsafe_allow_html=True
    )
    
    # Título principal
    st.title("🍷 Descubre el Sabor de España con CatemosVino")

    # Descripción
    st.markdown(
    """
    ### Conectamos bodegas con mercados internacionales
    En **CatemosVino**, llevamos la esencia del vino español al mundo. Somos una empresa especializada en la exportación de vinos con **Denominación de Origen**, 
    conectando bodegas excepcionales con mercados internacionales en busca de calidad y autenticidad.
    
    Si eres una bodega que busca expandir sus horizontes y llevar sus vinos a nuevos mercados, estamos aquí para hacerlo posible. 
    Nuestro equipo de expertos en exportación y distribución trabaja con una red global de importadores, distribuidores y amantes del vino, 
    asegurando que cada botella encuentre su destino perfecto.
    """
)

    # Beneficios
    st.subheader("🍇 ¿Por qué elegir CatemosVino?")
    benefits = [
    "✅ Especialización en vinos con Denominación de Origen",
    "✅ Acceso a mercados internacionales estratégicos",
    "✅ Asesoramiento personalizado en exportación",
    "✅ Red global de compradores y distribuidores",
]
    st.write("\n".join(benefits))

    # Llamado a la acción
    st.markdown(
    """
    ---
    ### 🚀 Únete a nosotros y lleva la riqueza del vino español más allá de nuestras fronteras
    **Conversemos sobre cómo hacer crecer tu bodega juntos.**
    
    📩 **Contáctanos hoy y descubre nuevas oportunidades de exportación.**
    """
)

    # Formulario de contacto
    st.subheader("📩 Contáctanos")
    with st.form("contact_form"):
        name = st.text_input("Nombre de la Bodega o Contacto")
        email = st.text_input("Correo Electrónico")
        message = st.text_area("Mensaje")
        submit_button = st.form_submit_button("Enviar Consulta")
    
    if submit_button:
        st.success("¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.")    

with tab2:
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

with tab3:
    st.title("Qué Ofrecemos")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        mundo = "data/img/mundo.png"
        if mundo:
            st.image(mundo, use_container_width=False)
    st.markdown("""
                En **CatemosVino** nos apasiona el mundo del vino y por ello ofrecemos una selecta gama de vinos españoles de alta calidad, procedentes de bodegas dirigidas por productores y enólogos comprometidos con la excelencia. Nuestro catálogo está cuidadosamente elaborado, incluyendo proyectos de pequeña y mediana escala, así como vinos de edición limitada, donde cada etiqueta refleja la esencia de una tierra, la dedicación de familias y un arraigo que se transmite en cada sorbo.

    Asimismo, en **CatemosVino** seleccionamos y comercializamos vinos que destacan por su excelente relación calidad/precio, fundamentados en nuestro profundo conocimiento de los productores y en una constante actualización respecto a las necesidades y tendencias del mercado. Nuestra colaboración con un grupo de bodegas profesionales nos permite ofrecer un porfolio atractivo y completo, complementando nuestra oferta con vinos que se adaptan a diferentes gustos y ocasiones.

    El reconocimiento y la valoración de nuestros clientes son la mejor muestra de nuestro compromiso con la calidad y la pasión por el vino español. En **CatemosVino**, trabajamos día a día para brindarte una experiencia única, donde la tradición se une con la innovación, y cada botella cuenta una historia singular.
    """)

with tab4:
    # definimos una imagen y sobreponemos un titulo
    image_bww = 'https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/feria_bww-t.png'
    #titular = "🍷 La Importancia de las Ferias del Vino en la Exportación Española"

    # Usamos HTML y CSS
    st.markdown(
        f"""
        <style>
        .image-container {{
            position: relative;
            display: inline-block;
            width: 100%;
            text-align: center;
        }}
        .image-container img {{
            width: 100%;
            height: auto;
            display: block;
            border-radius: 10px;
        }}
        .overlay-text {{
            position: relative;
            top: 0%;
            left: 15%;
            transform: translate(-15%, -750%);
            color: white;
            font-size: 48px;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 0.3);
            padding: 0px 0;
            text-align: center;
            border-radius: 10px;
        }}
        </style>
        <div class="image-container">
            <img src="{image_bww}" alt="WWB: Feria de Vino" title="Feria de Vino">
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown("""
Las ferias del vino son **eventos clave para la internacionalización del vino español**, ya que permiten a las bodegas presentar sus productos, establecer contactos comerciales y expandirse a nuevos mercados globales.

Participar en estos eventos facilita:

✅ **Promoción y visibilidad global**, destacando la calidad y diversidad del vino español.  
✅ **Acceso a compradores estratégicos**, incluyendo importadores, distribuidores y minoristas.  
✅ **Oportunidad de cierre de contratos comerciales** y expansión a nuevos mercados.  
✅ **Identificación de tendencias globales**, como vinos ecológicos, premium y digitales.  
✅ **Refuerzo de la marca y el prestigio del vino español** en mercados clave.  

Para las bodegas españolas, participar en ferias como **Vinitaly, ProWein, Vinexpo, Fenavin y Barcelona Wine Week** es fundamental para la internacionalización del sector. Cada una ofrece ventajas únicas:

✅ **Vinitaly** → Acceso al mercado italiano y oportunidades en mercados emergentes.  
✅ **ProWein** → Exposición global y contacto con importadores clave.  
✅ **Vinexpo** → Posicionamiento en segmentos premium y acceso a mercados de lujo.  
✅ **Fenavin** → Plataforma dedicada a la exportación del vino español.  
✅ **Barcelona Wine Week** → Conexión con compradores internacionales y enfoque en tendencias actuales.

**Para cualquier bodega española que busque expandir su presencia internacional, estas ferias son herramientas imprescindibles.** 🚀🍷            
            """)

    st.markdown("---")

    st.markdown("### 🍷 Principales Ferias Europeas para la Exportación del Vino Español")

    # Vinitaly
    st.markdown("""
#### 📍 [Vinitaly (Verona, Italia)](https://www.vinitaly.com/en/)

**Descripción:**  
Vinitaly es una de las ferias de vino más prestigiosas del mundo, celebrada anualmente en Verona. Es un punto de encuentro esencial para productores, importadores, distribuidores, restauradores, técnicos, periodistas y líderes de opinión, que se reúnen para conocer las tendencias del mercado, degustar vinos y establecer relaciones comerciales.

**Beneficios para las bodegas españolas:**

- **Acceso al mercado italiano e internacional:** Italia es uno de los principales consumidores de vino, y Vinitaly atrae a compradores de Europa, Asia y América, ofreciendo oportunidades para la exportación.
- **Presentación de vinos premium y ecológicos:** La feria es ideal para destacar vinos de alta gama y sostenibles, segmentos en crecimiento en el mercado global.
- **Networking de alto nivel:** Posibilidad de interactuar con profesionales influyentes y líderes de opinión del sector vitivinícola.

**Próxima edición:**  
6 al 9 de abril de 2025.
""")

    # ProWein
    st.markdown("""
#### 📍 [ProWein (Düsseldorf, Alemania)](https://www.prowein.com/)

**Descripción:**  
ProWein es reconocida como la feria internacional más importante para vinos y licores. Celebrada en Düsseldorf, reúne a productores y distribuidores de todo el mundo, ofreciendo una plataforma para negocios y tendencias en la industria vitivinícola.

**Beneficios para las bodegas españolas:**

- **Exposición global:** Con participantes de más de 60 países, ProWein ofrece una audiencia internacional diversa.
- **Oportunidades comerciales:** Facilita el contacto directo con importadores y distribuidores clave de mercados como EE.UU., China y Europa.
- **Descubrimiento de tendencias:** Es el lugar ideal para conocer las últimas tendencias en vinos, desde variedades emergentes hasta innovaciones en producción y marketing.

**Próxima edición:**  
16 al 18 de marzo de 2025.
""")

    # Vinexpo
    st.markdown("""
#### 📍 [Vinexpo (París, Francia)](https://wineparis.com/)

**Descripción:**  
Vinexpo Paris es una feria líder dedicada a los profesionales del vino y las bebidas espirituosas. Ofrece una plataforma para el networking, la innovación y el descubrimiento de nuevas tendencias en la industria.

**Beneficios para las bodegas españolas:**

- **Acceso a mercados premium:** Francia es un mercado competitivo, pero Vinexpo permite a las bodegas españolas posicionar sus vinos en segmentos de lujo y alta gastronomía.
- **Conexiones internacionales:** Atrae a compradores de Asia y América, facilitando la expansión a estos mercados.
- **Visibilidad frente a competidores europeos:** Oportunidad para destacar la calidad y diversidad de los vinos españoles frente a productores franceses e italianos.

**Próxima edición:**  
10 al 12 de febrero 2025.
""")

    # Fenavin
    st.markdown("""
#### 📍 [Fenavin (Ciudad Real, España)](https://www.fenavin.com/)

**Descripción:**  
Fenavin es la feria de referencia del vino español, centrada en la promoción y exportación de vinos nacionales. Es un punto de encuentro para productores españoles y compradores internacionales.

**Beneficios para las bodegas españolas:**

- **Foco en la exportación:** Diseñada específicamente para impulsar la presencia internacional del vino español.
- **Amplia participación internacional:** Asisten compradores de más de 100 países, ofreciendo oportunidades para expandir mercados.
- **Apoyo a pequeñas y medianas bodegas:** Plataforma ideal para que bodegas emergentes presenten sus productos a una audiencia global.

**Próxima edición:**  
6 al 8 de mayo de 2025.
""")

    # Barcelona Wine Week
    st.markdown("""
#### 📍 [Barcelona Wine Week (Barcelona, España)](https://www.barcelonawineweek.com/en/)

**Descripción:**  
La Barcelona Wine Week es una feria emergente que se ha consolidado como una plataforma clave para la internacionalización del vino español. Se celebra en la vibrante ciudad de Barcelona y destaca por su enfoque en la calidad, la innovación y la sostenibilidad.

**Beneficios para las bodegas españolas:**

- **Conexión con compradores internacionales:** Gracias a la ubicación estratégica de Barcelona, la feria atrae a importadores, distribuidores y minoristas de todo el mundo.
- **Enfoque en la diversidad y autenticidad:** BWW pone en valor la riqueza de las Denominaciones de Origen españolas, ayudando a posicionar los vinos en segmentos premium.
- **Atención a tendencias y sostenibilidad:** La feria destaca las nuevas tendencias de consumo, como los vinos ecológicos y biodinámicos, que tienen una demanda creciente en mercados internacionales.

**Próxima edición:**  
3 al 5 de febrero de 2025.
""")

with tab5:
    st.title("Nuestros Vinos Españoles D.O.")

    # Cargar datos desde el CSV
    df = pd.read_csv('data/webs_vinos.csv')

    # Número de columnas por fila
    num_columnas = 3

    # Crear una lista de columnas
    columnas = st.columns(num_columnas)

    # CSS para mejorar la presentación
    st.markdown("""
        <style>
            .image-card {
                text-align: center;
                background: #f9f9f9;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .image-card img {
                width: 100%;
                max-width: 170px;
                height: auto;
                border-radius: 5px;
            }
            .image-card a {
                text-decoration: none;
                color: #333;
                font-weight: bold;
                display: block;
                margin-top: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Mostrar las imágenes distribuidas en 3 columnas
    for i, (idx, row) in enumerate(df.iterrows()):
        col = columnas[i % num_columnas]  # Distribuir en columnas uniformemente
        with col:
            st.markdown(
                f"""
                <div class="image-card">
                    <a href="{row['Web']}" target="_blank">
                        <img src="{row['Imagen']}" alt="{row['Nombre']}" title="{row['Nombre']}">
                        <div>{row['Nombre']}</div>
                    </a>
                </div>
                """, unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)

with tab6:
    image_EDA = 'https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/EDA_banner.png'
    st.markdown(
        f"""
        <style>
        .image-container {{
            position: relative;
            display: inline-block;
            width: 100%;
            text-align: center;
        }}
        .image-container img {{
            width: 100%;
            height: auto;
            display: block;
            border-radius: 10px;
        }}

        </style>
        <div class="image-container">
            <img src="{image_EDA}" alt="Nuestros Vinos, descubrelo en la seccion de Vinos" title="Nuestros Vinos, descubrelo en la seccion de Vinos">
        </div>
        """, unsafe_allow_html=True
    )
    
# Estilos personalizados para las imágenes
    st.markdown("""
    <style>
        .image-card2 {
            text-align: center;
            background: #f9f9f9;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 25px;
            transition: transform 0.2s ease-in-out;
        }
        .image-card2:hover {
            transform: scale(1.0);
        }
        .image-card2 img {
            width: 100%;
            max-width: 900px;
            height: auto;
            border-radius: 8px;
        }
        .image-title2 {
            font-weight: bold;
            font-size: 16px;
            margin-top: 10px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

    with st.container():
        st.title("📊 Exploratory Data Analysis (EDA)")

    st.markdown("""
    Este análisis explora la **producción, consumo, exportación e importación de vino** en diferentes países.  
    Se destacan las principales tendencias observadas en los datos.
    """)

    # Función para mostrar imágenes con estilo
    def show_image_card(img_url, title):
        st.markdown(
            f"""
            <div class="image-card2">
                <img src="{img_url}" alt="{title}">
                <div class="image-title2">{title}</div>
            </div>
            """, unsafe_allow_html=True
        )

    # Sección de Producción
    st.subheader("📌 Producción de Vino por País")
    show_image_card("https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/produccion.png", 
                    "Producción de Vino")
    st.markdown("""
    - **Italia, España y Francia** son los mayores productores de vino.  
    - La producción de vino es relativamente estable debido a las características de la viticultura.
    """)

    # Sección de Consumo
    st.subheader("🍷 Consumo de Vino por País")
    show_image_card("https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/consumo.png", 
                    "Consumo de Vino")
    st.markdown("""
    - **Estados Unidos** es el mayor consumidor de vino a nivel mundial.  
    - El consumo de vino está más distribuido en comparación con la producción.
    """)

    # Sección de Exportación
    st.subheader("🚢 Exportación de Vino por País")
    show_image_card("https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/exportacion.png", 
                    "Exportación de Vino")
    st.markdown("""
    - **España e Italia** lideran la exportación de vino.  
    - Francia también exporta, pero en menor cantidad.
    """)

    # Sección de Importación
    st.subheader("📦 Importación de Vino por País")
    show_image_card("https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/importacion.png", 
                    "Importación de Vino")
    st.markdown("""
    - **Estados Unidos, Reino Unido y Alemania** son los principales importadores de vino.  
    - Francia, a pesar de ser un gran exportador, también importa vino.
    """)

    # Sección de Exportaciones de España
    st.subheader("📦 Exportaciones de España a otros Países")
    show_image_card("https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/exportaciones_DOP.png", 
                    "Exportaciones de España")
    st.markdown("""
    - **Reino Unido, Alemania y Estados Unidos** son los principales destinos de exportación de España.  
    """)


with tab7: #PowerBI
    powerbi_utl = 'https://app.powerbi.com/view?r=eyJrIjoiOTZiOGIwMzItN2VlOC00YmQ5LTllYjItMTY2OTJjOTRhNDJkIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=517520207b6e9083ca82'
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <iframe src="{powerbi_utl}" width="1024" height="612" frameborder="0" allowFullScreen="true"></iframe>
        </div>
        """, unsafe_allow_html=True
    )

with tab8: #ML

    image_ML = 'https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/ML_banner.png'
    st.markdown(
        f"""
        <style>
        .image-container {{
            position: relative;
            display: inline-block;
            width: 100%;
            text-align: center;
        }}
        .image-container img {{
            width: 100%;
            height: auto;
            display: block;
            border-radius: 10px;
        }}

        </style>
        <div class="image-container">
            <img src="{image_ML}" alt="ML de prediccion" title="ML de prediccion">
        </div>
        """, unsafe_allow_html=True
    )

 # Configurar la API de Azure ML
    URL = 'http://645d3dd2-f2ae-46c8-923c-605c1bb30cc7.westus2.azurecontainer.io/score'
    API_KEY = 'uqFnQy2rfrItFthgW6rqfESfvzMsl6iy'

# Función para obtener predicción desde Azure ML
    def get_prediction(data):
        body = str.encode(json.dumps(data))
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + API_KEY}
        req = urllib.request.Request(URL, body, headers)

        try:
            response = urllib.request.urlopen(req)
            result = json.loads(response.read())
            return result
        except urllib.error.HTTPError as error:
            st.error(f"❌ La solicitud falló con código de estado: {error.code}")
            st.text(error.read().decode("utf8", 'ignore'))
            return None

# Configuración de la aplicación Streamlit
    st.title("🍷 Predicción del Importe por Venta de Vino")
    st.write("Introduce los detalles de la venta para estimar el importe.")

# Selección de DOPs
    DOPs = st.selectbox("📍 Denominación de Origen Protegida (DOPs)", ["Abadía Retuerta", "Abona", "Alella", "Alicante", "Almansa", "Arlanza", "Arribes", "Aylés", "Bierzo", "Binissalem",
    "Bolandin", "Bullas", "Calatayud", "Calzadilla", "Campo de Borja", "Campo de la Guardia", "Cangas", "Cariñena",
    "Casa del Blanco", "Cataluña", "Cava", "Cebreros", "Chacolí de Álava", "Chacolí de Bizkaia", "Chacolí de Getaria",
    "Chozas Carrascal", "Cigales", "Conca de Barberá", "Condado de Huelva", "Costers del Segre", "Dehesa del Carrizal",
    "Dehesa Peñalba", "Dominio de Valdepusa", "El Hierro", "El Terrerazo", "Empordà", "Finca Élez", "Gran Canaria",
    "Granada", "Guijoso", "Islas Canarias", "Jerez-Xérès-Sherry", "Jumilla", "La Gomera", "La Mancha", "La Palma",
    "Lanzarote", "Lebrija", "León", "Los Balagueses", "Málaga", "Manchuela", "Manzanilla S.B.", "Méntrida", "Mondéjar",
    "Monterrei", "Montilla-Moriles", "Montsant", "Navarra", "Pago de Arínzano", "Pago de Otazu", "Pago El Vicario",
    "Pago Florentino", "Pago La Jaraba", "Pago Los Cerrillos", "Pago Vallegarcía", "Penedés", "Pla de Bages",
    "Pla i Llevant", "Prado de Irache", "Priorat", "Rías Baixas", "Ribeira Sacra", "Ribeiro", "Ribera del Duero",
    "Ribera del Guadiana", "Ribera del Júcar", "Rioja", "Rueda", "Sierra de Salamanca", "Sierras de Málaga", "Somontano",
    "Tacoronte-Acentejo", "Tarragona", "Terra Alta", "Tierra del Vino de Zamora", "Toro", "Uclés", "Urueña",
    "Utiel-Requena", "Valdeorras", "Valdepeñas", "Valencia", "Valle de Güímar", "Valle de la Orotava", "Valles de Benavente",
    "Valtiendas", "Vera de Estenas", "Vinos de Madrid", "Ycoden-Daute-Isora", "Yecla"])
    Year = st.number_input("📆 Año de Venta", min_value=2000, max_value=2050, value=2025, step=1)
    cantidad_vino = st.number_input("🍷 Cantidad de vino a vender (en hectolitros)", min_value=1, max_value=1000000, step=1)

# Lista de países a los que se puede vender
    countries = ["Alemania", "Austria", "Belgica", "Bulgaria", "Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "Estonia",
                "Finlandia", "Francia", "Grecia", "Holanda", "Hungria", "Irlanda", "Italia", "Letonia", "Lituania", "Luxemburgo",
                "Malta", "Polonia", "Portugal", "Republica_Checa", "Rumania", "Suecia", "Noruega", "Suiza", "Reino_Unido", "Rusia",
                "Resto_Europa_no_E.U.", "Argentina", "Brasil", "Canada", "Colombia", "EE.UU.", "Mexico", "Venezuela", "Resto_America",
                "Corea", "China", "India", "Japon", "Resto_Asia", "Australia", "Resto_Oceania", "Resto_Paises"]

# Selección del país al que vender
    country_selected = st.selectbox("🌍 ¿A qué país deseas vender?", countries)

# Diccionario de países con valores iniciales en 0
    country_values = {country: 0 for country in countries}

# Si selecciona un país, se asigna la cantidad de vino a vender
    if country_selected != "No vender":
        country_values[country_selected] = cantidad_vino

# Lista de tipologías de vino
    wine_types = ["Blanco", "Rosado", "Tinto", "De_licor", "Espumoso", "De_aguja", "Otros"]

# Selección de tipología de vino
    wine_selected = st.selectbox("🍾 ¿Qué tipo de vino deseas vender?", wine_types)

# Diccionario de tipos de vino con valores iniciales en 0
    wine_values = {wine: 0 for wine in wine_types}
    wine_values[wine_selected] = cantidad_vino

# Datos de la petición
    data = {
        "Inputs": {
            "data": [
                {
                    "DOPs": DOPs,
                    "Year": Year,
                    **country_values,
                    **wine_values,
                }
            ]
        }
    }

# Botón de predicción
    if st.button("💰 Calcular Importe"):
        result = get_prediction(data)

        if result and "Results" in result and isinstance(result["Results"], list) and len(result["Results"]) > 0:
            importe = round(result["Results"][0], 2)  # Redondeamos a 2 decimales
            st.success(f"💰 **Importe estimado:** {importe} € por la venta de 1 hectolitros de {wine_selected} de {DOPs} en {Year}, vendido a {country_selected}.")
        else:
            st.error("❌ La respuesta de la API no contiene datos válidos.")

# Pie de página
st.markdown("---")
st.markdown("### Explorando el mundo del vino con pasión y calidad.")
image_foot_t1 = 'https://raw.githubusercontent.com/Xicu980/WineProject/refs/heads/main/data/img/nuestros_vinos.png'
st.markdown(
        f"""
        <style>
        .image-container {{
            position: relative;
            display: inline-block;
            width: 100%;
            text-align: center;
        }}
        .image-container img {{
            width: 100%;
            height: auto;
            display: block;
            border-radius: 10px;
        }}

        </style>
        <div class="image-container">
            <img src="{image_foot_t1}" alt="Nuestros Vinos, descubrelo en la seccion de Vinos" title="Nuestros Vinos, descubrelo en la seccion de Vinos">
        </div>
        """, unsafe_allow_html=True
)
st.markdown("📌 *CatemosVino - Exportación de vinos de calidad.*")