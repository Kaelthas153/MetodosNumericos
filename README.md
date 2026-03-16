# Métodos Numéricos - Tarea 2, 3 y 4

Este repositorio contiene el desarrollo y la implementación de sistemas de ecuaciones lineales resueltos mediante tres métodos iterativos fundamentales: **Gradiente Conjugado (CG)**, **Sobre-relajación Sucesiva (SOR)** y **Gauss-Seidel**.

---

## 📂 Contenido del Proyecto

* **`Tarea3.py`**: Script de Python que resuelve el sistema planteado en la Tarea 2. Muestra el desarrollo paso a paso (iteración por iteración) en la consola.
* **`Tarea4.xlsx`**: Hoja de cálculo que contiene las tablas de iteraciones, los valores de las variables en cada paso y el cálculo del error residual para los tres métodos.
* **`Métodos númericos.pdf`**: Documento con el planteamiento teórico, la justificación del sistema elegido y la solución exacta conocida.
* **`requirements.txt`**: Archivo de configuración que lista las librerías necesarias (como NumPy) para ejecutar los scripts.

---

## 🛠️ Instrucciones de Ejecución (Tarea 3)

Para ejecutar la resolución del sistema en tu máquina local, sigue estos pasos:

1.  **Asegúrate de tener Python instalado.**
2.  **Instalar la librería necesaria (NumPy):**
    ```bash
    pip install numpy
    ```
3.  **Ejecutar el script:**
    ```bash
    python Tarea3.py
    ```

El programa mostrará en consola los resultados de cada iteración, permitiendo verificar la convergencia hacia la solución exacta: $$x = [1, 2, -1]^T$$.

---

## 📊 Descripción de los Métodos Utilizados

### 1. Gauss-Seidel
Es un método iterativo para resolver sistemas de ecuaciones lineales. Se diferencia del método de Jacobi porque utiliza los valores ya actualizados de las variables dentro de la misma iteración para calcular los siguientes.

### 2. Sobre-relajación Sucesiva (SOR)
Es una variante del método de Gauss-Seidel que introduce un factor de relajación $$\omega$$. En este proyecto se utilizó $$\omega = 1.05$$ para acelerar la velocidad de convergencia.

### 3. Gradiente Conjugado (CG)
Es un algoritmo para la solución numérica de sistemas de ecuaciones lineales cuyas matrices son simétricas y definidas positivas. Es un método de búsqueda que, teóricamente, alcanza la solución exacta en un número de pasos igual a la dimensión de la matriz.

---

## 📉 Resumen de Resultados (Tarea 4)
En la hoja de cálculo adjunta se observa cómo el **Gradiente Conjugado** converge con mayor precisión en menos pasos, mientras que **SOR** presenta una mejora notable en comparación con **Gauss-Seidel** estándar.

---
**Autor:** Kaelthas153  
**Curso:** Métodos Numéricos  
**Fecha:** Marzo 2026
