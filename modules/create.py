import streamlit as st

from utils.json_manager import cargar_productos, guardar_productos
from utils.logs import registrar_accion


# =========================
# PERMISOS
# =========================
def permitir_creacion():

    if st.session_state.rol not in ["admin", "usuario_2"]:
        st.error("⛔ No tienes permisos para crear productos")
        st.stop()


# =========================
# CREAR PRODUCTO
# =========================
def agregar_producto():

    permitir_creacion()

    st.title("➕ Crear producto")

    productos = cargar_productos()

    # =========================
    # FORMULARIO
    # =========================
    with st.form("form_create_product"):

        nombre = st.text_input("Nombre del producto")
        categoria = st.text_input("Categoría")
        precio = st.number_input("Precio", min_value=0.0, step=0.01)
        stock = st.number_input("Stock", min_value=0, step=1)
        marca = st.text_input("Marca")
        descripcion = st.text_area("Descripción")

        submitted = st.form_submit_button("Guardar producto")

    # =========================
    # GUARDAR PRODUCTO
    # =========================
    if submitted:

        if not nombre:
            st.error("❌ El nombre es obligatorio")
            return

        # Evitar duplicados
        if any(p["nombre"].lower() == nombre.lower() for p in productos):
            st.error("❌ Ya existe un producto con ese nombre")
            return

        nuevo_producto = {
            "id": max([p["id"] for p in productos], default=0) + 1,
            "nombre": nombre,
            "categoria": categoria,
            "precio": float(precio),
            "stock": int(stock),
            "marca": marca,
            "descripcion": descripcion
        }

        productos.append(nuevo_producto)
        guardar_productos(productos)

        # =========================
        # LOG
        # =========================
        registrar_accion(
            st.session_state.usuario,
            "CREATE PRODUCTO",
            f"{nombre} | Stock: {stock}"
        )

        st.success("✅ Producto creado correctamente")
        st.rerun()