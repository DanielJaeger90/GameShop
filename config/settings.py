import os


# =========================
# INFO DE LA APP
# =========================
APP_NAME = "Gaming Shop ERP"
APP_ICON = "🎮"
APP_VERSION = "1.0.0"


# =========================
# RUTAS BASE
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

PRODUCTOS_FILE = os.path.join(DATA_DIR, "productos.json")
USUARIOS_FILE = os.path.join(DATA_DIR, "usuarios.json")
VENTAS_FILE = os.path.join(DATA_DIR, "ventas.json")
LOGS_FILE = os.path.join(DATA_DIR, "logs.json")


# =========================
# ROLES DEL SISTEMA (UNIFICADO)
# =========================
ROLES = {
    "ADMIN": "admin",
    "USER_1": "usuario_1",
    "USER_2": "usuario_2"
}

ADMIN_ROLE = ROLES["ADMIN"]
USER_1_ROLE = ROLES["USER_1"]
USER_2_ROLE = ROLES["USER_2"]


# =========================
# PERMISOS CENTRALIZADOS
# =========================
PERMISOS = {
    "admin": ["create", "read", "update", "delete", "users", "orders"],
    "usuario_2": ["create", "read", "update", "delete", "orders"],
    "usuario_1": ["read", "orders"]
}


# =========================
# REGLAS DE NEGOCIO INVENTARIO
# =========================
STOCK_CRITICO = 5
SIN_STOCK = 0


# =========================
# TIENDAS
# =========================
TIENDAS = ["Tienda_1", "Tienda_2"]


# =========================
# UI CONFIG
# =========================
THEME = {
    "background": "#0e1117",
    "sidebar": "#161b22",
    "primary": "#238636",
    "accent": "#58a6ff"
}