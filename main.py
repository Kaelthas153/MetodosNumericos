import streamlit as st
import numpy as np

st.set_page_config(page_title="Tarea 6 - Métodos Iterativos", layout="wide")

# --- PANTALLA 1: CONFIGURACIÓN PRINCIPAL ---
st.title("🧮 Configuración del Sistema Lineal")
st.markdown("---")

col_input, col_info = st.columns([1, 1])

with col_input:
    st.subheader("1. Ingrese los coeficientes de la Matriz A")
    # Usamos el ejemplo de la Tarea 2 como default
    a11 = st.number_input("A[1,1]", value=10.0)
    a12 = st.number_input("A[1,2]", value=-1.0)
    a13 = st.number_input("A[1,3]", value=2.0)
    
    st.subheader("2. Ingrese el vector b")
    b1 = st.number_input("b[1]", value=6.0)
    b2 = st.number_input("b[2]", value=25.0)
    b3 = st.number_input("b[3]", value=-11.0)

with col_info:
    st.subheader("3. Parámetros de Control")
    total_iter = st.slider("Máximo de iteraciones a calcular", 1, 20, 5)
    omega = st.number_input("Factor de Relajación (SOR)", value=1.05, step=0.05)
    st.info("Solución esperada para el ejemplo default: [1, 2, -1]")

# Construcción de la matriz
A = np.array([[a11, a12, a13], [-1, 11, -1], [2, -1, 10]], dtype=float)
b = np.array([b1, b2, b3], dtype=float)

# --- NAVEGACIÓN POR MÉTODOS ---
st.markdown("---")
pestana_gs, pestana_sor, pestana_cg = st.tabs(["Gauss-Seidel", "SOR", "Gradiente Conjugado"])

# --- MÉTODO 1: GAUSS-SEIDEL ---
with pestana_gs:
    st.header("Visualización: Gauss-Seidel")
    x = np.zeros(3)
    gs_pasos = [x.copy()]
    for _ in range(total_iter):
        for j in range(3):
            suma = b[j] - np.dot(A[j, :j], x[:j]) - np.dot(A[j, j+1:], x[j+1:])
            x[j] = suma / A[j, j]
        gs_pasos.append(x.copy())
    
    paso_gs = st.select_slider("Moverse entre iteraciones (GS)", options=range(len(gs_pasos)), key="gs_slider")
    st.metric(f"Vector x en iteración {paso_gs}", f"[{gs_pasos[paso_gs][0]:.4f}, {gs_pasos[paso_gs][1]:.4f}, {gs_pasos[paso_gs][2]:.4f}]")

# --- MÉTODO 2: SOR ---
with pestana_sor:
    st.header(f"Visualización: SOR (ω={omega})")
    x_s = np.zeros(3)
    sor_pasos = [x_s.copy()]
    for _ in range(total_iter):
        for j in range(3):
            suma = b[j] - np.dot(A[j, :j], x_s[:j]) - np.dot(A[j, j+1:], x_s[j+1:])
            x_gs = suma / A[j, j]
            x_s[j] = (1 - omega) * x_s[j] + omega * x_gs
        sor_pasos.append(x_s.copy())
        
    paso_sor = st.select_slider("Moverse entre iteraciones (SOR)", options=range(len(sor_pasos)), key="sor_slider")
    st.metric(f"Vector x en iteración {paso_sor}", f"[{sor_pasos[paso_sor][0]:.4f}, {sor_pasos[paso_sor][1]:.4f}, {sor_pasos[paso_sor][2]:.4f}]")

# --- MÉTODO 3: GRADIENTE CONJUGADO ---
with pestana_cg:
    st.header("Visualización: Gradiente Conjugado")
    x_c = np.zeros(3)
    r = b - np.dot(A, x_c)
    p = r.copy()
    cg_pasos = [x_c.copy()]
    for _ in range(total_iter):
        alpha = np.dot(r, r) / np.dot(p, np.dot(A, p))
        x_c = x_c + alpha * p
        r_n = r - alpha * np.dot(A, p)
        beta = np.dot(r_n, r_n) / np.dot(r, r)
        p = r_n + beta * p
        r = r_n
        cg_pasos.append(x_c.copy())

    paso_cg = st.select_slider("Moverse entre iteraciones (CG)", options=range(len(cg_pasos)), key="cg_slider")
    st.metric(f"Vector x en iteración {paso_cg}", f"[{cg_pasos[paso_cg][0]:.4f}, {cg_pasos[paso_cg][1]:.4f}, {cg_pasos[paso_cg][2]:.4f}]")
