import streamlit as st


# =========================
# VERIFICAR LOGIN
# =========================
def require_login():

    if "usuario" not in st.session_state or st.session_state.usuario is None:
        st.error("⛔ Debes iniciar sesión para acceder al sistema")
        st.stop()


# =========================
# VERIFICAR ROL
# =========================
def require_role(roles_permitidos):

    if st.session_state.rol not in roles_permitidos:
        st.error("⛔ No tienes permisos para acceder a esta sección")
        st.stop()


# =========================
# OBTENER USUARIO ACTUAL
# =========================
def get_user():

    return st.session_state.get("usuario", None)


# =========================
# OBTENER ROL ACTUAL
# =========================
def get_role():

    return st.session_state.get("rol", None)


# =========================
# ES ADMIN
# =========================
def is_admin():

    return st.session_state.get("rol") == "admin"


# =========================
# ES GESTOR (usuario_2 o admin)
# =========================
def is_manager():

    return st.session_state.get("rol") in ["admin", "usuario_2"]