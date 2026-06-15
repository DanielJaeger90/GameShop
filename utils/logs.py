import json
import os
from datetime import datetime


# =========================
# ARCHIVO DE LOGS
# =========================
LOG_FILE = "data/logs.json"


# =========================
# CARGAR LOGS
# =========================
def cargar_logs():

    if not os.path.exists(LOG_FILE):
        return []

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


# =========================
# GUARDAR LOGS
# =========================
def guardar_logs(logs):

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4, ensure_ascii=False)


# =========================
# REGISTRAR ACCIÓN
# =========================
def registrar_accion(usuario, accion, detalle=""):

    logs = cargar_logs()

    nuevo_log = {
        "id": len(logs) + 1,
        "usuario": usuario,
        "accion": accion,
        "detalle": detalle,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    logs.append(nuevo_log)

    guardar_logs(logs)