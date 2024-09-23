import numpy as np
import matplotlib.pyplot as plt

class NewtonRaphsonMethod:
    def __init__(self, f, df, x0, tol=1e-5):
        self.f = f
        self.df = df
        self.x0 = x0
        self.tol = tol
        self.root = None
        self.iterations = 0
        self.x_history = [x0]  # Guardar el historial de x para graficar

    def solve(self):
        x = self.x0
        while abs(self.f(x)) > self.tol:
            # Guardar cada valor de x para poder graficarlo después
            self.x_history.append(x)
            
            # Calcular el siguiente valor de x usando el método de Newton-Raphson
            x = x - self.f(x) / self.df(x)
            self.iterations += 1

        self.root = x
        self.x_history.append(x)  # Guardar el valor final

    def plot(self):
        # Crear valores de x para la función
        x_vals = np.linspace(self.x0 - 2, self.x0 + 2, 100)
        y_vals = self.f(x_vals)
        
        # Graficar la función f(x)
        plt.plot(x_vals, y_vals, label="f(x)", color='blue')
        plt.axhline(0, color='black', linewidth=0.5)

        # Graficar las rectas secantes en cada iteración
        for i in range(len(self.x_history) - 1):
            x_curr = self.x_history[i]
            y_curr = self.f(x_curr)
            slope = self.df(x_curr)  # Derivada en el punto actual
            
            # Crear una recta secante con la pendiente y el punto (x_curr, f(x_curr))
            secant_x_vals = np.linspace(x_curr - 1, x_curr + 1, 10)
            secant_y_vals = slope * (secant_x_vals - x_curr) + y_curr
            
            # Graficar la secante
            plt.plot(secant_x_vals, secant_y_vals, '--', label=f'Secante iter {i+1}', color='orange')

        plt.title(f"Raíz: {self.root} - Iteraciones: {self.iterations}")
        plt.legend()
        plt.show()
