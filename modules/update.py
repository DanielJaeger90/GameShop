import streamlit as st

from utils.json_manager import cargar_productos, guardar_productos
from utils.logs import registrar_accion


# =========================
# PERMISOS
# =========================
def permitir_actualizacion():

    if st.session_state.rol not in ["admin", "usuario_2"]:
        st.error("⛔ No tienes permisos para actualizar productos")
        st.stop()


# =========================
# ACTUALIZAR PRODUCTO
# =========================
def actualizar_producto():

    permitir_actualizacion()

    st.title("✏️ Actualizar producto")

    productos = cargar_productos()

    if not productos:
        st.warning("No hay productos disponibles")
        return

    # =========================
    # SELECCIÓN PRODUCTO
    # =========================
    opciones = [
        f"{p['id']} - {p['nombre']} (Stock: {p['stock']})"
        for p in productos
    ]

    seleccionado = st.selectbox("Selecciona producto", opciones)

    prod_id = int(seleccionado.split(" - ")[0])

    producto = next((p for p in productos if p["id"] == prod_id), None)

    if not producto:
        st.error("Producto no encontrado")
        return

    # =========================
    # FORMULARIO EDICIÓN
    # =========================
    with st.form("form_update_product"):

        nombre = st.text_input("Nombre", value=producto["nombre"])
        categoria = st.text_input("Categoría", value=producto["categoria"])
        precio = st.number_input("Precio", value=float(producto["precio"]), step=0.01)
        stock = st.number_input("Stock", value=int(producto["stock"]), step=1)
        marca = st.text_input("Marca", value=producto.get("marca", ""))
        descripcion = st.text_area("Descripción", value=producto.get("descripcion", ""))

        submitted = st.form_submit_button("Actualizar producto")

    # =========================
    # GUARDAR CAMBIOS
    # =========================
    if submitted:

        for p in productos:
            if p["id"] == prod_id:
                p["nombre"] = nombre
                p["categoria"] = categoria
                p["precio"] = float(precio)
                p["stock"] = int(stock)
                p["marca"] = marca
                p["descripcion"] = descripcion

        guardar_productos(productos)

        # =========================
        # LOG
        # =========================
        registrar_accion(
            st.session_state.usuario,
            "UPDATE PRODUCTO",
            f"{nombre} | Stock: {stock} | Precio: {precio}"
        )

        st.success("✅ Producto actualizado correctamente")
        st.rerun()