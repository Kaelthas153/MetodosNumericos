# Métodos Numéricos

Este repositorio contiene la implementación y documentación de diversos métodos numéricos para la resolución de sistemas de ecuaciones lineales y análisis de convergencia, desarrollados como parte del plan de estudios del curso.

---

## Aplicación Interactiva (Tarea 6)
Puedes acceder a la versión web de la aplicación desplegada en Streamlit a través del siguiente enlace:
👉 [Link de la aplicación en Streamlit](https://metodosnumericos-bjppwca8m5a7s5u3v5fepk.streamlit.app/)

---

## Contenido del Repositorio
El repositorio está organizado de la siguiente manera:

* **Tarea3.py**: Script de Python diseñado para ejecución en consola (CLI).
* **Tarea4.xlsx**: Archivo de Excel con cálculos comparativos y análisis de errores.
* **tarea6.py**: Aplicación interactiva desarrollada con el framework Streamlit.
* **Métodos númericos.pdf**: Documentación técnica detallada y reportes de resultados.
* **requirements.txt**: Listado de dependencias necesarias para el entorno de ejecución.

---

## Instrucciones de Uso Local

Para ejecutar los scripts en tu entorno local, sigue estos pasos:

1.  **Instalar dependencias:**
    Asegúrate de tener Python instalado y ejecuta el siguiente comando para instalar las librerías necesarias (como `numpy`):
    ```bash
    pip install numpy streamlit
    ```

2.  **Ejecutar Script de Consola (Tarea 3):**
    ```bash
    python Tarea3.py
    ```

3.  **Ejecutar Aplicación Interactiva (Tarea 6):**
    ```bash
    streamlit run tarea6.py
    ```

---

## Descripción de los Métodos

### 1. Gauss-Seidel
Es un método iterativo utilizado para resolver sistemas de ecuaciones lineales $Ax = b$. A diferencia del método de Jacobi, utiliza los valores actualizados de las variables tan pronto como están disponibles en la iteración actual, lo que acelera la convergencia.

### 2. Sobrerrelajación Sucesiva (SOR)
Es una variante del método de Gauss-Seidel que busca acelerar la convergencia mediante un factor de relajación $\omega$. Para este proyecto, se ha determinado un valor óptimo de $\omega = 1.05$. La fórmula de actualización es:
$$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)} \right)$$

### 3. Gradiente Conjugado
Es un algoritmo para la solución numérica de sistemas de ecuaciones lineales cuyas matrices son simétricas y definidas positivas. Se basa en la minimización de la función cuadrática:
$$f(x) = \frac{1}{2}x^T Ax - b^T x$$
Utilizando direcciones de búsqueda ortogonales (conjugadas) respecto a la matriz $A$.

---

## Conclusiones (Tarea 4)
Tras el análisis realizado en el archivo Excel, se concluye que:
* **Eficiencia:** El método de **Gradiente Conjugado** presenta la mayor velocidad de convergencia en sistemas de gran escala y matrices dispersas.
* **Optimización:** El uso de **SOR con $\omega = 1.05$** reduce significativamente el número de iteraciones necesarias en comparación con Gauss-Seidel estándar, aunque su estabilidad depende críticamente de la elección de dicho parámetro.

---

**Autor:** Kaelthas153  
**Curso:** Métodos Numéricos  
**Fecha:** Marzo 2026
