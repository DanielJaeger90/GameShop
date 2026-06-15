import streamlit as st

from utils.json_manager import cargar_productos, guardar_productos
from utils.sales_manager import registrar_venta
from utils.logs import registrar_accion


# =========================
# PERMISOS
# =========================
def permitir_pedido():

    if st.session_state.rol not in ["usuario_2", "usuario_1"]:
        st.error("⛔ No tienes permisos para realizar pedidos")
        st.stop()


# =========================
# OBTENER PRODUCTO
# =========================
def obtener_producto(productos, prod_id):

    for p in productos:
        if p["id"] == prod_id:
            return p
    return None


# =========================
# CREAR PEDIDO
# =========================
def crear_pedido():

    permitir_pedido()

    st.title("🛒 Crear pedido")

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

    producto = obtener_producto(productos, prod_id)

    if not producto:
        st.error("Producto no encontrado")
        return

    # =========================
    # VALIDACIÓN STOCK
    # =========================
    if producto["stock"] <= 0:
        st.error("🚫 Producto sin stock")
        return

    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        max_value=int(producto["stock"]),
        step=1
    )

    tienda = st.selectbox("Tienda destino", ["Tienda_1", "Tienda_2"])

    # =========================
    # CONFIRMAR PEDIDO
    # =========================
    if st.button("Confirmar pedido"):

        # doble seguridad de stock
        producto_actual = obtener_producto(productos, prod_id)

        if cantidad > producto_actual["stock"]:
            st.error("❌ Stock insuficiente (posible cambio reciente)")
            return

        # =========================
        # DESCONTAR STOCK
        # =========================
        for p in productos:
            if p["id"] == prod_id:
                p["stock"] -= cantidad

        guardar_productos(productos)

        # =========================
        # CALCULAR TOTAL
        # =========================
        total = float(producto["precio"]) * cantidad

        # =========================
        # REGISTRAR VENTA
        # =========================
        registrar_venta(
            st.session_state.usuario,
            producto["nombre"],
            cantidad,
            tienda,
            total
        )

        # =========================
        # LOG SISTEMA
        # =========================
        registrar_accion(
            st.session_state.usuario,
            "VENTA",
            f"{producto['nombre']} | Cantidad: {cantidad} | {tienda}"
        )

        st.success(
            f"✅ Pedido realizado: {cantidad} x {producto['nombre']} → {tienda}"
        )

        st.rerun()