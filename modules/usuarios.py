import streamlit as st
import pandas as pd

from utils.json_manager import cargar_usuarios, guardar_usuarios
from utils.logs import registrar_accion


# =========================
# PERMISOS
# =========================
def permitir_gestion_usuarios():

    if st.session_state.rol != "admin":
        st.error("⛔ Solo el ADMIN puede gestionar usuarios")
        st.stop()


# =========================
# GESTIÓN DE USUARIOS
# =========================
def gestion_usuarios():

    permitir_gestion_usuarios()

    st.title("👥 Gestión de usuarios")

    usuarios = cargar_usuarios()

    df = pd.DataFrame(usuarios)

    # =========================
    # LISTADO
    # =========================
    st.subheader("📋 Usuarios actuales")
    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # =========================
    # CREAR USUARIO
    # =========================
    st.subheader("➕ Crear nuevo usuario")

    with st.form("form_create_user"):

        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        rol = st.selectbox("Rol", ["admin", "usuario_1", "usuario_2"])

        crear = st.form_submit_button("Crear usuario")

    if crear:

        if not usuario or not password:
            st.error("❌ Usuario y contraseña obligatorios")
            return

        if any(u["usuario"] == usuario for u in usuarios):
            st.error("❌ Este usuario ya existe")
            return

        nuevo_usuario = {
            "usuario": usuario,
            "password": password,
            "rol": rol
        }

        usuarios.append(nuevo_usuario)
        guardar_usuarios(usuarios)

        registrar_accion(
            st.session_state.usuario,
            "CREATE USER",
            f"{usuario} ({rol})"
        )

        st.success("✅ Usuario creado correctamente")
        st.rerun()

    st.markdown("---")

    # =========================
    # ELIMINAR USUARIO
    # =========================
    st.subheader("❌ Eliminar usuario")

    opciones = [u["usuario"] for u in usuarios if u["usuario"] != "admin"]

    usuario_sel = st.selectbox("Selecciona usuario", opciones)

    confirmar = st.checkbox("Confirmo eliminación")

    if confirmar and st.button("Eliminar usuario"):

        usuarios = [u for u in usuarios if u["usuario"] != usuario_sel]

        guardar_usuarios(usuarios)

        registrar_accion(
            st.session_state.usuario,
            "DELETE USER",
            f"{usuario_sel}"
        )

        st.success("✅ Usuario eliminado correctamente")
        st.rerun()