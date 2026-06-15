import streamlit as st


# =========================
# CSS GLOBAL (DARK MODE ERP)
# =========================
def cargar_css():

    st.markdown("""
    <style>

    /* ===== FONDO GENERAL ===== */
    .stApp {
        background-color: #0e1117;
        color: #e6edf3;
    }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
    }

    /* ===== TITULOS ===== */
    h1, h2, h3 {
        color: #58a6ff;
    }

    /* ===== BOTONES ===== */
    .stButton > button {
        background-color: #238636;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #2ea043;
    }

    /* ===== INPUTS ===== */
    input, textarea, select {
        border-radius: 8px !important;
    }

    /* ===== TARJETAS DASHBOARD ===== */
    .card {
        background-color: #161b22;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
    }

    /* ===== TABLAS ===== */
    .dataframe {
        border-radius: 10px;
    }

    /* ===== ALERTAS PERSONALIZADAS ===== */
    .success-box {
        background-color: #0f5132;
        padding: 10px;
        border-radius: 8px;
        color: white;
    }

    .warning-box {
        background-color: #664d03;
        padding: 10px;
        border-radius: 8px;
        color: white;
    }

    .error-box {
        background-color: #842029;
        padding: 10px;
        border-radius: 8px;
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)


# =========================
# BADGE DE ROL
# =========================
def badge_rol(rol: str):

    colores = {
        "admin": "#f85149",
        "usuario_2": "#f59e0b",
        "usuario_1": "#58a6ff"
    }

    color = colores.get(rol, "#58a6ff")

    return f"""
    <span style="
        background-color:{color};
        padding:5px 10px;
        border-radius:8px;
        color:white;
        font-weight:bold;
        font-size:12px;">
        {rol.upper()}
    </span>
    """


# =========================
# CSS EXTRA POR ROL (VISUAL)
# =========================
def aplicar_css_por_rol(rol):

    colores = {
        "admin": "#f85149",
        "usuario_2": "#f59e0b",
        "usuario_1": "#58a6ff"
    }

    color = colores.get(rol, "#58a6ff")

    st.markdown(f"""
    <style>
        .role-bar {{
            border-left: 5px solid {color};
            padding-left: 10px;
            margin-bottom: 10px;
        }}
    </style>
    """, unsafe_allow_html=True)