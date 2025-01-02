import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate

# Definir la variable simbólica
x = symbols('x')

# Definir la función para la integral
funcion = x**2

# Calcular la integral simbólicamente
resultado = integrate(funcion, (x, 0, 1))  # Integral entre 0 y 1
print(f"El resultado de la integral es: {resultado}")

# Graficar la función
x_vals = np.linspace(0, 1, 100)
y_vals = x_vals**2

# Graficar la función y el área bajo la curva
plt.plot(x_vals, y_vals, label="y = x^2")
plt.fill_between(x_vals, y_vals, color='skyblue', alpha=0.4)

# Títulos y etiquetas
plt.title("Área bajo la curva \(y = x^2\)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Mostrar el gráfico
plt.show()
