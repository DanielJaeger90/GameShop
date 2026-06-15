import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.json_manager import cargar_productos, cargar_usuarios
from utils.sales_manager import cargar_ventas
from utils.logs import cargar_logs


# =========================
# DASHBOARD PRINCIPAL
# =========================
def mostrar_dashboard():

    st.title("📊Menu principal")

    # =========================
    # CARGA DE DATOS
    # =========================
    productos = cargar_productos()
    usuarios = cargar_usuarios()
    ventas = cargar_ventas()
    logs = cargar_logs()

    df_p = pd.DataFrame(productos)
    df_u = pd.DataFrame(usuarios)
    df_v = pd.DataFrame(ventas)
    df_l = pd.DataFrame(logs)

    # =========================
    # SEGURIDAD DATAFRAME
    # =========================
    if df_p.empty:
        st.warning("No hay productos en el sistema")
        return

    # =========================
    # KPIs PRINCIPALES
    # =========================
    total_productos = len(df_p)
    stock_total = df_p["stock"].sum()
    valor_inventario = (df_p["precio"] * df_p["stock"]).sum()

    stock_critico = len(df_p[df_p["stock"] < 5])
    sin_stock = len(df_p[df_p["stock"] == 0])

    total_ventas = len(df_v) if not df_v.empty else 0
    ingresos = df_v["total"].sum() if not df_v.empty else 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📦 Productos", total_productos)
    col2.metric("📊 Stock total", stock_total)
    col3.metric("💰 Ventas", total_ventas)
    col4.metric("💶 Ingresos", f"{ingresos:.2f} €")

    st.markdown("---")

    # =========================
    # ALERTAS
    # =========================
    st.subheader("🚨 Alertas del sistema")

    if sin_stock > 0:
        st.error(f"🚨 {sin_stock} productos sin stock")

    if stock_critico > 0:
        st.warning(f"⚠️ {stock_critico} productos con stock crítico")

    if sin_stock == 0 and stock_critico == 0:
        st.success("✔ Inventario en estado óptimo")

    st.markdown("---")

    # =========================
    # GRÁFICO: PRODUCTOS POR CATEGORÍA
    # =========================
    st.subheader("📦 Productos por categoría")

    categorias = df_p["categoria"].value_counts()

    fig1, ax1 = plt.subplots()
    categorias.plot(kind="bar", ax=ax1)
    ax1.set_ylabel("Cantidad")
    ax1.set_xlabel("Categoría")

    st.pyplot(fig1)

    st.markdown("---")



    # =========================
    # RANKING PRODUCTOS MÁS VENDIDOS
    # =========================
    st.subheader("🏆 Productos más vendidos")

    if not df_v.empty:
        ranking = df_v["producto"].value_counts().head(5)
        st.bar_chart(ranking)
    else:
        st.info("No hay ventas registradas aún")

    st.markdown("---")

    # =========================
    # HISTORIAL DE VENTAS
    # =========================
    st.subheader("🛒 Historial de ventas")

    if not df_v.empty:
        st.dataframe(df_v, use_container_width=True)
    else:
        st.info("Sin ventas todavía")

    st.markdown("---")

    # =========================
    # LOGS DEL SISTEMA
    # =========================
    st.subheader("🧾 Actividad del sistema")

    if not df_l.empty:
        st.dataframe(df_l.sort_values("fecha", ascending=False), use_container_width=True)
    else:
        st.info("No hay actividad registrada")