import streamlit as st
import pandas as pd

from utils.json_manager import cargar_productos


# =========================
# LISTAR PRODUCTOS
# =========================
def listar_productos():

    st.title("📋 Catálogo de productos")

    productos = cargar_productos()

    if not productos:
        st.warning("No hay productos disponibles")
        return

    df = pd.DataFrame(productos)

    # =========================
    # BUSCADOR
    # =========================
    st.subheader("🔎 Buscar producto")

    busqueda = st.text_input("Escribe nombre o categoría")

    if busqueda:
        df = df[
            df["nombre"].str.contains(busqueda, case=False, na=False) |
            df["categoria"].str.contains(busqueda, case=False, na=False)
        ]

    # =========================
    # FILTRO STOCK
    # =========================
    st.sidebar.subheader("🎛️ Filtros")

    solo_stock = st.sidebar.checkbox("Solo con stock")

    if solo_stock:
        df = df[df["stock"] > 0]

    # =========================
    # ORDENAR
    # =========================
    ordenar = st.sidebar.selectbox(
        "Ordenar por",
        ["id", "nombre", "categoria", "precio", "stock"]
    )

    df = df.sort_values(by=ordenar)

    # =========================
    # ALERTAS VISUALES
    # =========================
    st.markdown("---")

    for _, row in df.iterrows():

        if row["stock"] == 0:
            estado = "🔴 SIN STOCK"
        elif row["stock"] < 5:
            estado = "🟠 STOCK CRÍTICO"
        else:
            estado = "🟢 OK"

        st.markdown(f"""
        ### {row['nombre']}
        🏷️ Categoría: {row['categoria']}  
        💰 Precio: {row['precio']} €  
        📦 Stock: {row['stock']}  
        📊 Estado: {estado}  
        ---
        """)

    # =========================
    # TABLA COMPLETA
    # =========================
    st.subheader("📊 Vista en tabla")

    st.dataframe(df, use_container_width=True)