import json
import os


# =========================
# RUTAS BASE
# =========================
BASE_DIR = "data"

PRODUCTOS_FILE = os.path.join(BASE_DIR, "productos.json")
USUARIOS_FILE = os.path.join(BASE_DIR, "usuarios.json")


# =========================
# LECTURA GENÉRICA
# =========================
def leer_json(ruta):

    if not os.path.exists(ruta):
        return []

    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================
# ESCRITURA GENÉRICA
# =========================
def guardar_json(ruta, datos):

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


# =========================
# PRODUCTOS
# =========================
def cargar_productos():
    return leer_json(PRODUCTOS_FILE)


def guardar_productos(productos):
    guardar_json(PRODUCTOS_FILE, productos)


# =========================
# USUARIOS
# =========================
def cargar_usuarios():
    return leer_json(USUARIOS_FILE)


def guardar_usuarios(usuarios):
    guardar_json(USUARIOS_FILE, usuarios)