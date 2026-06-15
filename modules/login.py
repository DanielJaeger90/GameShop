import streamlit as st

from utils.json_manager import cargar_usuarios


# =========================
# LOGIN
# =========================
def login():

    st.title("🔐 Acceso al sistema")
    st.markdown("Introduce tus credenciales para entrar")

    usuarios = cargar_usuarios()

    # =========================
    # FORMULARIO
    # =========================
    with st.form("login_form"):

        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        submit = st.form_submit_button("Entrar")

    # =========================
    # VALIDACIÓN
    # =========================
    if submit:

        user_found = None

        for u in usuarios:
            if u["usuario"] == usuario and u["password"] == password:
                user_found = u
                break

        if user_found:

            st.session_state.usuario = user_found["usuario"]
            st.session_state.rol = user_found["rol"]

            st.success(f"✔ Bienvenido {user_found['usuario']} ({user_found['rol']})")

            st.rerun()

        else:
            st.error("❌ Usuario o contraseña incorrectos")


# =========================
# LOGOUT
# =========================
def logout():

    if st.sidebar.button("🚪 Cerrar sesión"):

        st.session_state.usuario = None
        st.session_state.rol = None

        st.rerun()