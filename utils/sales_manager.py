import json
import os
from datetime import datetime

# =========================
# ARCHIVO DE VENTAS
# =========================
SALES_FILE = "data/ventas.json"


# =========================
# CARGAR VENTAS
# =========================
def cargar_ventas():

    if not os.path.exists(SALES_FILE):
        return []

    with open(SALES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================
# GUARDAR VENTAS
# =========================
def guardar_ventas(ventas):

    with open(SALES_FILE, "w", encoding="utf-8") as f:
        json.dump(ventas, f, indent=4, ensure_ascii=False)


# =========================
# REGISTRAR VENTA
# =========================
def registrar_venta(usuario, producto, cantidad, tienda, total):

    ventas = cargar_ventas()

    nueva_venta = {
        "id": len(ventas) + 1,
        "usuario": usuario,
        "producto": producto,
        "cantidad": cantidad,
        "tienda": tienda,
        "total": float(total),
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    ventas.append(nueva_venta)

    guardar_ventas(ventas)