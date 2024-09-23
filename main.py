import tkinter as tk
from tkinter import messagebox
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from methods.Newton import NewtonRaphsonMethod
from methods.bisection import Bisection
from tkinter import simpledialog

class NumericalMethodsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Métodos Numéricos")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Campo de entrada para la función
        # Botones para seleccionar el método
        newton_button = tk.Button(self.root, text="Método de Newton-Raphson", command=self.run_newton)
        newton_button.pack(pady=10)

        biseccion_button = tk.Button(self.root, text="Método de Bisección", command=self.run_biseccion)
        biseccion_button.pack(pady=10)


    def validar_funcion(self, expression):
        for i in expression:
            if i == "^":
                expression = expression.replace(i, "**")
        try:
            func = parse_expr(expression)
            return func
        except Exception as e:
            messagebox.showerror("Error", f"La función ingresada no es válida: {str(e)}")
            return None
        
    def mostrar_funcion(self):
        messagebox.showinfo("Función", self.ingresar_funcion())
    
    def run_biseccion(self):
        expression = simpledialog.askstring("Bisección", "Ingrese la función:")
        a = simpledialog.askfloat("Bisección", "Ingrese el valor de a:")
        b = simpledialog.askfloat("Bisección", "Ingrese el valor de b:")
        func = self.validar_funcion(expression)

        if func:
            x = sp.symbols('x')
            f = sp.lambdify(x, func, "numpy")
            method = Bisection(f, a, b, 1e-5)
            method.solve()
            messagebox.showinfo("Resultado Bisección", f"Raíz: {method.root}, Iteraciones: {method.iterations}")
            method.plot()
    def run_newton(self):
        # Obtener la expresión ingresada por el usuario
      
        expression = simpledialog.askstring("Newton-Raphson", "Ingrese la función:")
        x0 = simpledialog.askfloat("Newton-Raphson", "Ingrese el valor de x0:")
        func = self.validar_funcion(expression)

        if func:
            x = sp.symbols('x')
            derivative = sp.diff(func, x)
            
            # Convertir las funciones a Python para usarlas en los métodos numéricos
            f = sp.lambdify(x, func, "numpy")
            df = sp.lambdify(x, derivative, "numpy")

            # Ejecutar el método de Newton-Raphson
            method = NewtonRaphsonMethod(f, df, x0, 1e-5)  # Inicializar con x0 = 1.5
            method.solve()
            messagebox.showinfo("Resultado Newton-Raphson", f"Raíz: {method.root}, Iteraciones: {method.iterations}")
            method.plot()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumericalMethodsApp(root)
    root.mainloop()
