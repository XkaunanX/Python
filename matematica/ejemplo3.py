import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, integrate

# Definir las variables simbólicas
x, y, z = symbols('x y z')

# Definir la función para la integral triple
funcion = x**2 + y**2 + z**2

# Calcular la integral triple simbólicamente
integral_interna = integrate(funcion, (z, 0, 1))  # Integral respecto a z
integral_externa = integrate(integral_interna, (y, 0, 1))  # Integral respecto a y
resultado = integrate(integral_externa, (x, 0, 1))  # Integral respecto a x

print(f"El resultado de la integral triple es: {resultado}")

# Graficar la función sobre el volumen
x_vals = np.linspace(0, 1, 50)
y_vals = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# Definir la función como un array
Z = X**2 + Y**2

# Crear la figura 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
surface = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', alpha=0.8)

# Etiquetas y título
ax.set_title("Integral Triple: Área bajo \(x^2 + y^2 + z^2\)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")

# Barra de color
fig.colorbar(surface, shrink=0.5, aspect=10)

# Mostrar el gráfico
plt.show()
