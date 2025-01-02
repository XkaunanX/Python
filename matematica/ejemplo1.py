import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, integrate

# Definir las variables simbólicas
x, y = symbols('x y')

# Definir la función
funcion = x**2 + y**2

# Calcular la integral doble simbólicamente
integral_interna = integrate(funcion, (y, 0, x))  # Integral respecto a y
resultado = integrate(integral_interna, (x, 0, 1))  # Integral respecto a x

print(f"El resultado de la integral es: {resultado}")

# Graficar la función y la región
x_vals = np.linspace(0, 1, 100)
y_vals = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Definir la función como un array
Z = X**2 + Y**2

# Enmascarar valores fuera del límite (y <= x)
Z[Y > X] = np.nan

# Crear la figura 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

# Etiquetas y título
ax.set_title("Integral Doble: Área bajo (x² + y²)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")

# Barra de color
fig.colorbar(surface, shrink=0.5, aspect=10)

# Mostrar el gráfico
plt.show()