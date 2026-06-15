import streamlit as st

from utils.json_manager import cargar_productos, guardar_productos
from utils.logs import registrar_accion


# =========================
# PERMISOS
# =========================
def permitir_eliminacion():

    if st.session_state.rol not in ["admin", "usuario_2"]:
        st.error("⛔ No tienes permisos para eliminar productos")
        st.stop()


# =========================
# ELIMINAR PRODUCTO
# =========================
def eliminar_producto():

    permitir_eliminacion()

    st.title("❌ Eliminar producto")

    productos = cargar_productos()

    if not productos:
        st.warning("No hay productos disponibles")
        return

    # =========================
    # SELECCIÓN
    # =========================
    opciones = [
        f"{p['id']} - {p['nombre']} (Stock: {p['stock']})"
        for p in productos
    ]

    seleccionado = st.selectbox("Selecciona producto a eliminar", opciones)

    prod_id = int(seleccionado.split(" - ")[0])

    producto = next((p for p in productos if p["id"] == prod_id), None)

    if not producto:
        st.error("Producto no encontrado")
        return

    # =========================
    # CONFIRMACIÓN
    # =========================
    st.warning(f"⚠️ Estás a punto de eliminar: **{producto['nombre']}**")

    confirmar = st.checkbox("Confirmo que quiero eliminar este producto")

    # =========================
    # ELIMINAR
    # =========================
    if confirmar and st.button("Eliminar producto"):

        productos = [p for p in productos if p["id"] != prod_id]

        guardar_productos(productos)

        # =========================
        # LOG
        # =========================
        registrar_accion(
            st.session_state.usuario,
            "DELETE PRODUCTO",
            f"{producto['nombre']} eliminado"
        )

        st.success("✅ Producto eliminado correctamente")
        st.rerun()