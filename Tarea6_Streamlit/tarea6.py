import streamlit as st
import numpy as np
import pandas as pd

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Tarea 6 - Caso Real", layout="wide")

st.title("🌡️ Aplicación de Métodos Numéricos")
st.markdown("**Caso de Estudio:** Distribución de temperatura en una aleta de enfriamiento (Nodos=5).")
st.write("Modifica los coeficientes de la Matriz $A$ y el vector $b$ para ver cómo cambia la solución.")

# --- DATOS POR DEFECTO ---
default_A = np.array([
    [4.0, -1.0, 0.0, 0.0, 0.0],
    [-1.0, 4.0, -1.0, 0.0, 0.0],
    [0.0, -1.0, 4.0, -1.0, 0.0],
    [0.0, 0.0, -1.0, 4.0, -1.0],
    [0.0, 0.0, 0.0, -1.0, 4.0]
])
default_b = np.array([20.0, 40.0, 60.0, 80.0, 160.0])
x_exacto = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Matriz de Coeficientes (A)")
    df_A = pd.DataFrame(default_A, columns=["x1", "x2", "x3", "x4", "x5"])
    A_editada = st.data_editor(df_A, use_container_width=True).to_numpy()

with col2:
    st.subheader("Vector de Términos Indep. (b)")
    df_b = pd.DataFrame(default_b, columns=["b"])
    b_editado = st.data_editor(df_b, use_container_width=True).to_numpy().flatten()

# --- BARRA LATERAL ---
st.sidebar.header("⚙️ Parámetros")
total_iter = st.sidebar.slider("Número máximo de iteraciones", 1, 20, 5)
omega = st.sidebar.number_input("Factor SOR (ω)", value=1.15, step=0.05)
n = len(b_editado)

# --- PANTALLAS DE MÉTODOS ---
st.markdown("---")
tab_gs, tab_sor, tab_cg = st.tabs(["Gauss-Seidel", "SOR", "Gradiente Conjugado"])

# 1. GAUSS-SEIDEL
with tab_gs:
    x = np.zeros(n)
    hist_gs = [x.copy()]
    for _ in range(total_iter):
        for j in range(n):
            suma = b_editado[j] - np.dot(A_editada[j, :j], x[:j]) - np.dot(A_editada[j, j+1:], x[j+1:])
            x[j] = suma / A_editada[j, j]
        hist_gs.append(x.copy())
    
    val = st.select_slider("Iteración a visualizar (GS)", options=range(len(hist_gs)), key="gs")
    st.metric("Resultado x", f"{np.round(hist_gs[val], 4)}")

# 2. SOR
with tab_sor:
    x_s = np.zeros(n)
    hist_sor = [x_s.copy()]
    for _ in range(total_iter):
        for j in range(n):
            suma = b_editado[j] - np.dot(A_editada[j, :j], x_s[:j]) - np.dot(A_editada[j, j+1:], x_s[j+1:])
            x_gs_val = suma / A_editada[j, j]
            x_s[j] = (1 - omega) * x_s[j] + omega * x_gs_val
        hist_sor.append(x_s.copy())
    
    val_s = st.select_slider("Iteración a visualizar (SOR)", options=range(len(hist_sor)), key="sor")
    st.metric("Resultado x", f"{np.round(hist_sor[val_s], 4)}")

# 3. GRADIENTE CONJUGADO
with tab_cg:
    x_c = np.zeros(n)
    r = b_editado - np.dot(A_editada, x_c)
    p = r.copy()
    hist_cg = [x_c.copy()]
    
    try:
        for _ in range(total_iter):
            alpha = np.dot(r, r) / np.dot(p, np.dot(A_editada, p))
            x_c = x_c + alpha * p
            r_n = r - alpha * np.dot(A_editada, p)
            beta = np.dot(r_n, r_n) / np.dot(r, r)
            p = r_n + beta * p
            r = r_n
            hist_cg.append(x_c.copy())
        
        val_c = st.select_slider("Iteración a visualizar (CG)", options=range(len(hist_cg)), key="cg")
        st.metric("Resultado x", f"{np.round(hist_cg[val_c], 4)}")
    except Exception:
        st.error("Error: La matriz editada no es simétrica definida positiva.")

st.sidebar.markdown("---")
st.sidebar.success(f"**Solución Exacta:**\n{x_exacto}")

# --- EXPORTAR A EXCEL (CSV) ---
st.markdown("---")
st.header("📥 Descargar Resultados Generados")

def generar_csv_descarga(A, b, total_iter, omega, n):
    rows = []
    
    # GS
    rows.append(["MÉTODO: GAUSS-SEIDEL"])
    rows.append(["Iteración"] + [f"x{i+1}" for i in range(n)])
    x = np.zeros(n)
    rows.append([0] + list(np.round(x, 4)))
    for i in range(1, total_iter + 1):
        for j in range(n):
            suma = b[j] - np.dot(A[j, :j], x[:j]) - np.dot(A[j, j+1:], x[j+1:])
            x[j] = suma / A[j, j]
        rows.append([i] + list(np.round(x, 4)))
    
    rows.append([]) # Espacio
    
    # SOR
    rows.append([f"MÉTODO: SOR (w={omega})"])
    rows.append(["Iteración"] + [f"x{i+1}" for i in range(n)])
    x_s = np.zeros(n)
    rows.append([0] + list(np.round(x_s, 4)))
    for i in range(1, total_iter + 1):
        for j in range(n):
            suma = b[j] - np.dot(A[j, :j], x_s[:j]) - np.dot(A[j, j+1:], x_s[j+1:])
            x_gs_val = suma / A[j, j]
            x_s[j] = (1 - omega) * x_s[j] + omega * x_gs_val
        rows.append([i] + list(np.round(x_s, 4)))
        
    rows.append([]) # Espacio
    
    # GRADIENTE CONJUGADO
    rows.append(["MÉTODO: GRADIENTE CONJUGADO"])
    rows.append(["Iteración"] + [f"x{i+1}" for i in range(n)])
    x_c = np.zeros(n)
    r = b - np.dot(A, x_c)
    p = r.copy()
    rows.append([0] + list(np.round(x_c, 4)))
    try:
        for i in range(1, total_iter + 1):
            alpha = np.dot(r, r) / np.dot(p, np.dot(A, p))
            x_c = x_c + alpha * p
            r_n = r - alpha * np.dot(A, p)
            beta = np.dot(r_n, r_n) / np.dot(r, r)
            p = r_n + beta * p
            r = r_n
            rows.append([i] + list(np.round(x_c, 4)))
    except Exception:
        rows.append(["Error: Matriz no válida para CG en esta descarga."])

    # Convertir a texto CSV
    csv_text = ""
    for row in rows:
        csv_text += ",".join([str(item) for item in row]) + "\n"
    return csv_text

# Generar datos y crear el botón
csv_data = generar_csv_descarga(A_editada, b_editado, total_iter, omega, n)

st.download_button(
    label="📄 Descargar Tabla de Iteraciones (CSV)",
    data=csv_data,
    file_name="Resultados_Iterativos.csv",
    mime="text/csv",
)
