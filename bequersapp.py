import streamlit as st
import base64
from PIL import Image
import webbrowser

# --------- CONFIGURACIÓN DE PÁGINA ---------
st.set_page_config(page_title="Portal Bequers", layout="wide", page_icon="https://www.bequers.es/themes/beckers/assets/img/favicon.ico")

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

# --------- FONDO PERSONALIZADO CON GRADIENTE ---------
def set_background():
    background_image = "https://www.bequers.es/storage/app/media/hero-beckers-big.png"
    gradient = "linear-gradient(rgba(0, 0, 128, 0.3), rgba(0, 0, 128, 0.3))"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {gradient}, url("{background_image}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

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

# --------- BOTONES CON IMÁGENES ---------
cols = st.columns(3)

for i, app in enumerate(apps):
    with cols[i % 3]:
        st.image(app["img"], use_column_width="always", caption=app["name"])
        if st.button(f"🚀 Ir a {app['name']}", key=app["name"]):
            webbrowser.open_new_tab(app["url"])
