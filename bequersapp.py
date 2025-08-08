import streamlit as st
from PIL import Image
import webbrowser

# --------- CONFIGURACIÓN DE PÁGINA ---------
st.set_page_config(
    page_title="Portal Bequers",
    layout="wide",
    page_icon="https://www.bequers.es/themes/beckers/assets/img/favicon.ico"
)

# --------- FONDO PERSONALIZADO CON GRADIENTE 50% ---------
def set_background():
    background_image = "https://www.bequers.es/storage/app/media/hero-beckers-big.png"
    gradient = "linear-gradient(rgba(0, 0, 128, 0.5), rgba(0, 0, 128, 0.5))"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {gradient}, url("{background_image}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* BOTONES CON EFECTO HOVER */
        .stButton>button {{
            background-color: #ffffff10;
            color: white;
            border: 1px solid #ffffff40;
            transition: all 0.3s ease;
        }}

        .stButton>button:hover {{
            box-shadow: 0 0 10px 3px #ffffffaa;
            border: 1px solid #ffffff80;
            background-color: #ffffff30;
            color: #fff;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Aplicamos fondo desde el inicio para que funcione también en el login
set_background()

# --------- SISTEMA DE LOGIN ---------
USERS = {
    "admin": "1234",
    "usuario": "clave"
}

def login():
    st.sidebar.image("https://www.bequers.es/themes/beckers/assets/img/favicon.ico", width=80)
    st.sidebar.markdown("## Iniciar sesión")
    username = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")
    if st.sidebar.button("Entrar"):
        if username in USERS and USERS[username] == password:
            st.session_state["login"] = True
        else:
            st.sidebar.error("Usuario o contraseña incorrectos")

if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    login()
    st.stop()

# --------- TÍTULO CON LOGO ---------
st.markdown(
    """
    <div style='display: flex; align-items: center; margin-bottom: 30px;'>
        <img src="https://www.bequers.es/themes/beckers/assets/img/favicon.ico" style="height: 50px; margin-right: 20px;" />
        <h1 style='color: white;'>Portal de Aplicaciones Bequers</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# --------- URLS Y LOGOS ---------
apps = [
    {
        "name": "Guías Azerca",
        "url": "https://guiasazerca.streamlit.app/",
        "img": "images/guiasazerca.png"
    },
    {
        "name": "Bequers Captación",
        "url": "https://bequerscaptacion.streamlit.app/",
        "img": "images/bequerscaptacion.png"
    },
    {
        "name": "Novel Generar",
        "url": "https://novelgenerar.streamlit.app/",
        "img": "images/novelgenerar.png"
    },
    {
        "name": "Sala Generar",
        "url": "https://salagenerar.streamlit.app/",
        "img": "images/salagenerar.png"
    },
    {
        "name": "Recupón Generar",
        "url": "https://recupongenerar.streamlit.app/",
        "img": "images/recupongenerar.png"
    }
]

# --------- BOTONES CON IMÁGENES REDUCIDAS Y EFECTO HOVER ---------
cols = st.columns(5)

for i, app in enumerate(apps):
    with cols[i]:
        try:
            image = Image.open(app["img"])
            width, height = image.size
            resized = image.resize((int(width * 0.2), int(height * 0.2)))
            st.image(resized, use_container_width=False)
        except Exception as e:
            st.error(f"❌ No se pudo cargar la imagen: {app['img']}")

        st.markdown(
            f"""
            <a href="{app['url']}" target="_blank">
                <button style='margin-top: 10px; width: 100%; font-weight: bold;'>🚀 Ir a {app['name']}</button>
            </a>
            """,
            unsafe_allow_html=True
        )


