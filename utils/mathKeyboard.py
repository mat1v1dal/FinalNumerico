import tkinter as tk
from tkinter import messagebox

class VirtualMathKeyboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teclado Virtual Matemático")

        # Entrada para mostrar la expresión matemática
        self.expression = ""
        self.function_display = None
        self.create_widgets()

    def create_widgets(self):
        # Campo para mostrar la expresión
        self.function_display = tk.Entry(self.root, font=('Arial', 24), width=25, borderwidth=2)
        self.function_display.pack(pady=20)

        # Crear el teclado
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Botones de números y variables
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 0), ('x', 4, 1)
        ]

        operators = [
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 4),
            ('(', 4, 0), (')', 4, 2), ('^', 4, 4)
        ]

        # Botones de funciones especiales
        special_buttons = [
            ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4),
            ('log', 5, 0), ('ln', 5, 1), ('sqrt', 5, 2)
        ]

        # Añadir los botones al teclado
        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=('Arial', 18), width=5, height=2,
                               command=lambda t=text: self.add_to_expression(t))
            button.grid(row=row, column=col)

        for (text, row, col) in operators:
            button = tk.Button(button_frame, text=text, font=('Arial', 18), width=5, height=2,
                               command=lambda t=text: self.add_to_expression(t))
            button.grid(row=row, column=col)

        for (text, row, col) in special_buttons:
            button = tk.Button(button_frame, text=text, font=('Arial', 18), width=5, height=2,
                               command=lambda t=text: self.add_to_expression(f'{t}('))
            button.grid(row=row, column=col)

        # Botones de acción
        equals_button = tk.Button(self.root, text="Evaluar", font=('Arial', 18), width=15, height=2, command=self.submit_expression)
        equals_button.pack(pady=10)

        clear_button = tk.Button(self.root, text="Limpiar", font=('Arial', 18), width=15, height=2, command=self.clear_expression)
        clear_button.pack(pady=10)

    def add_to_expression(self, value):
        """Añade a la expresión actual"""
        self.expression += value
        self.function_display.delete(0, tk.END)
        self.function_display.insert(tk.END, self.expression)

    def clear_expression(self):
        """Limpia la expresión actual"""
        self.expression = ""
        self.function_display.delete(0, tk.END)

    def submit_expression(self):
        """Devuelve la expresión para ser usada en el método numérico"""
        # Eliminar espacios para evitar problemas
        self.expression = self.expression.replace(" ", "")
        if self.expression:
            self.root.quit()  # Cerrar la ventana
        else:
            messagebox.showerror("Error", "Por favor ingresa una función válida")

    def get_expression(self):
        """Devuelve la expresión ingresada"""
        return self.expression

# Función para mostrar el teclado y obtener la función matemática
def get_math_expression():
    root = tk.Tk()
    app = VirtualMathKeyboardApp(root)
    root.mainloop()
    return app.get_expression()
