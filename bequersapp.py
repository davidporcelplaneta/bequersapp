import streamlit as st

# --------- CONFIGURACIÓN DE PÁGINA ---------
st.set_page_config(
    page_title="Portal Bequers",
    layout="wide",
    page_icon="https://www.bequers.es/themes/beckers/assets/img/favicon.ico"
)

# --------- FONDO CON GRADIENTE AZUL (50%) ---------
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

        .card {{
            background-color: rgba(0, 0, 0, 0.4);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            transition: 0.3s ease-in-out;
            box-shadow: 0 0 10px rgba(255,255,255,0.1);
            margin: 10px;
        }}

        .card:hover {{
            box-shadow: 0 0 15px rgba(255,255,255,0.5);
            transform: scale(1.05);
        }}

        .card img {{
            width: 60px;
            height: 60px;
            margin-bottom: 15px;
        }}

        .card a button {{
            background-color: #222;
            border: 1px solid #fff;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s ease-in-out;
        }}

        .card a button:hover {{
            background-color: #444;
            box-shadow: 0 0 10px white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# --------- LOGIN ---------
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

# --------- APPS ---------
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

# --------- TARJETAS CON HTML ---------
cols = st.columns(5)

for i, app in enumerate(apps):
    with cols[i]:
        st.markdown(
            f"""
            <div class="card">
                <img src="{app['img']}" alt="{app['name']}" />
                <a href="{app['url']}" target="_blank">
                    <button>🚀 Ir a {app['name']}</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
