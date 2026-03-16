import numpy as np

# Configuración del sistema de la Tarea 2
A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)
x_exacto = np.array([1, 2, -1], dtype=float)
x0 = np.zeros(len(b))
iteraciones = 3

def imprimir_paso(metodo, i, x):
    print(f"{metodo} - Iteración {i}: {x}")

# --- 1. GAUSS-SEIDEL ---
print("--- Ejecutando Gauss-Seidel ---")
x_gs = x0.copy()
for i in range(1, iteraciones + 1):
    for j in range(len(b)):
        suma = b[j] - np.dot(A[j, :j], x_gs[:j]) - np.dot(A[j, j+1:], x_gs[j+1:])
        x_gs[j] = suma / A[j, j]
    imprimir_paso("GS", i, x_gs.copy())

# --- 2. SOR (w = 1.05) ---
print("\n--- Ejecutando SOR (w=1.05) ---")
x_sor = x0.copy()
w = 1.05
for i in range(1, iteraciones + 1):
    for j in range(len(b)):
        suma = b[j] - np.dot(A[j, :j], x_sor[:j]) - np.dot(A[j, j+1:], x_sor[j+1:])
        x_gs_val = suma / A[j, j]
        x_sor[j] = (1 - w) * x_sor[j] + w * x_gs_val
    imprimir_paso("SOR", i, x_sor.copy())

# --- 3. GRADIENTE CONJUGADO ---
print("\n--- Ejecutando Gradiente Conjugado ---")
x_cg = x0.copy()
r = b - np.dot(A, x_cg)
p = r.copy()
for i in range(1, iteraciones + 1):
    alpha = np.dot(r, r) / np.dot(p, np.dot(A, p))
    x_cg = x_cg + alpha * p
    r_nuevo = r - alpha * np.dot(A, p)
    beta = np.dot(r_nuevo, r_nuevo) / np.dot(r, r)
    p = r_nuevo + beta * p
    r = r_nuevo
    imprimir_paso("CG", i, x_cg.copy())

print("\n--- Comparación Final ---")
print(f"Solución Exacta: {x_exacto}")