import pandas as pd
from io import BytesIO


# =========================
# EXPORTAR CSV
# =========================
def exportar_csv(df):
    return df.to_csv(index=False).encode("utf-8")


# =========================
# EXPORTAR EXCEL
# =========================
def exportar_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Productos")

    return output.getvalue()