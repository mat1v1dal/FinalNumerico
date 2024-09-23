import numpy as np
import matplotlib.pyplot as plt

class Bisection:
    def __init__(self, f, a, b, tol=1e-5):
        self.f = f
        self.a = a  # Extremo inferior del intervalo
        self.b = b  # Extremo superior del intervalo
        self.tol = tol
        self.root = None
        self.iterations = 0
        self.interval_history = [(a, b)]  # Guardar historial de intervalos

    def solve(self):
        a, b = self.a, self.b
        while abs(b - a) > self.tol:
            # Calcular el punto medio
            c = (a + b) / 2
            
            # Verificar el valor de la función en el punto medio
            if self.f(c) == 0:
                break
            elif self.f(a) * self.f(c) < 0:
                b = c  # El cero está en [a, c]
            else:
                a = c  # El cero está en [c, b]

            # Guardar el intervalo actual
            self.interval_history.append((a, b))
            self.iterations += 1

        # Asignar la raíz aproximada
        self.root = (a + b) / 2
        self.interval_history.append((a, b))  # Guardar el último intervalo

    def plot(self):
        # Crear valores de x para graficar la función
        x_vals = np.linspace(self.a - 1, self.b + 1, 100)
        y_vals = self.f(x_vals)

        # Graficar la función f(x)
        plt.plot(x_vals, y_vals, label="f(x)", color='blue')
        plt.axhline(0, color='black', linewidth=0.5)

        # Graficar los intervalos en cada iteración
        for i, (a, b) in enumerate(self.interval_history):
            plt.plot([a, b], [self.f(a), self.f(b)], 'ro--', label=f'Intervalo iter {i+1}')

        plt.title(f"Raíz: {self.root} - Iteraciones: {self.iterations}")
        plt.legend()
        plt.show()
