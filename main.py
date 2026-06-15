import streamlit as st

from modules.login import login, logout
from modules.dashboard import mostrar_dashboard
from modules.read import listar_productos
from modules.create import agregar_producto
from modules.update import actualizar_producto
from modules.delete import eliminar_producto
from modules.orders import crear_pedido
from modules.usuarios import gestion_usuarios

from utils.styles import cargar_css, aplicar_css_por_rol


# =========================
# CONFIG APP
# =========================
st.set_page_config(
    page_title="Gaming Shop",
    page_icon="🎮",
    layout="wide"
)


# =========================
# CSS GLOBAL
# =========================
cargar_css()


# =========================
# INICIALIZAR SESIÓN
# =========================
if "usuario" not in st.session_state:
    st.session_state.usuario = None

if "rol" not in st.session_state:
    st.session_state.rol = None


# =========================
# LOGIN
# =========================
if not st.session_state.usuario:
    login()
    st.stop()


# =========================
# SEGURIDAD CSS POR ROL
# =========================
aplicar_css_por_rol(st.session_state.rol)


# =========================
# DEBUG
# =========================
st.sidebar.write("👤 USER:", st.session_state.usuario)
st.sidebar.write("🛡️ ROL:", st.session_state.rol)


# =========================
# SIDEBAR
# =========================
st.sidebar.title("🎮 Gaming Shop ERP")

logout()

st.sidebar.markdown("---")


# =========================
# NORMALIZAR ROL (IMPORTANTE)
# =========================
rol = str(st.session_state.rol).strip().lower()


# =========================
# MENÚ BASE
# =========================
menu = [
    "📊 Menu Principal",
    "📋 Productos"
]


# =========================
# TODOS PUEDEN COMPRAR
# =========================
if rol in ["admin", "usuario_2", "usuario_1"]:
    menu.append("🛒 Crear pedido")


# =========================
# CRUD SOLO ADMIN + GESTOR
# =========================
if rol in ["admin", "usuario_2"]:
    menu.extend([
        "➕ Crear producto",
        "✏️ Actualizar producto",
        "❌ Eliminar producto"
    ])


# =========================
# USUARIOS SOLO ADMIN
# =========================
if rol == "admin":
    menu.append("👥 Usuarios")


# =========================
# SELECT MENU
# =========================
opcion = st.sidebar.selectbox("📂 Menú", menu)


# =========================
# RUTAS
# =========================
if opcion == "📊 Menu Principal":
    mostrar_dashboard()

elif opcion == "📋 Productos":
    listar_productos()

elif opcion == "🛒 Crear pedido":
    crear_pedido()

elif opcion == "➕ Crear producto":
    agregar_producto()

elif opcion == "✏️ Actualizar producto":
    actualizar_producto()

elif opcion == "❌ Eliminar producto":
    eliminar_producto()

elif opcion == "👥 Usuarios":
    gestion_usuarios()