import tkinter as tk
from tkinter import StringVar

class BalancedParenthesesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Paréntesis Balanceados")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        # Variables
        self.input_text = StringVar()
        self.result_text = StringVar(value="Ingrese una expresión")

        # Crear elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de título
        title_label = tk.Label(self.root, text="Validador de Paréntesis Balanceados", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        # Campo de entrada
        entry = tk.Entry(self.root, textvariable=self.input_text, font=("Arial", 12), width=30)
        entry.pack(pady=5)
        entry.bind("<KeyRelease>", self.validate_parentheses)

        # Etiqueta de resultado
        self.result_label = tk.Label(self.root, textvariable=self.result_text, font=("Arial", 12), width=30, height=2)
        self.result_label.pack(pady=10)

    def validate_parentheses(self, event=None):
        expression = self.input_text.get()
        if self.is_valid_parentheses(expression):
            self.result_text.set("Válido")
            self.result_label.config(bg="lightgreen", fg="green")
        else:
            self.result_text.set("No válido")
            self.result_label.config(bg="lightcoral", fg="red")

    @staticmethod
    def is_valid_parentheses(expression):
        stack = []
        for char in expression:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0


# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = BalancedParenthesesApp(root)
    root.mainloop()
    