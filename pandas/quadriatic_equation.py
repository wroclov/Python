import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np


class QuadraticEquationPlotter:
    def __init__(self, root):
        self.root = root
        self.root.title("Quadratic Equation Plotter")

        self.num_equations_label = tk.Label(self.root, text="Number of Equations:")
        self.num_equations_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        self.num_equations = tk.IntVar()
        self.num_equations.set(2)  # Default to 2 equations
        self.num_equations_entry = tk.Entry(self.root, textvariable=self.num_equations)
        self.num_equations_entry.grid(row=0, column=1, padx=10, pady=5)

        self.frame_equations = tk.Frame(self.root)
        self.frame_equations.grid(row=1, columnspan=2, padx=10, pady=10)

        self.plot_button = tk.Button(self.root, text="Plot Equations", command=self.plot_equations)
        self.plot_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.generate_button = tk.Button(self.root, text="Generate Equation Fields",
                                         command=self.generate_equation_fields)
        self.generate_button.grid(row=3, columnspan=2, padx=10, pady=10)

        self.entry_a, self.entry_b, self.entry_c = [], [], []
        self.equations = []

    def solve_quadratic(self, a, b, c):
        """ Solve quadratic equation ax^2 + bx + c = 0 """
        discriminant = b ** 2 - 4 * a * c

        # If discriminant is positive, there are two real roots
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2

        # If discriminant is zero, there is one real root (repeated root)
        elif discriminant == 0:
            root = -b / (2 * a)
            return root, root

        # If discriminant is negative, there are two complex roots
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            return root1, root2

    def plot_quadratic_equations(self):
        """ Plot multiple quadratic equations and their roots on the same chart """
        plt.figure(figsize=(10, 6))

        x = np.linspace(-10, 10, 400)

        legend_entries = []

        for idx, (a, b, c) in enumerate(self.equations, start=1):
            y = a * x ** 2 + b * x + c
            roots = self.solve_quadratic(a, b, c)

            line, = plt.plot(x, y, label=f'Equation {idx}: {a}x^2 + {b}x + {c}')

            root_labels = []
            for root in roots:
                if isinstance(root, complex):
                    root_labels.append(f'({root.real:.2f} + {root.imag:.2f}j)')
                else:
                    root_labels.append(f'{root:.2f}')

            equation_str = f'{a}x^2 + {b}x + {c} = 0'
            legend_entry = f'Equation {idx}: {equation_str}, Roots: {", ".join(root_labels)}'
            legend_entries.append((line, legend_entry))

        plt.legend([entry[0] for entry in legend_entries], [entry[1] for entry in legend_entries], loc='upper left')

        plt.title('Quadratic Equations and Their Roots')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)
        plt.show()

    def plot_equations(self):
        try:
            num = self.num_equations.get()
            self.equations = []

            for i in range(num):
                a = float(self.entry_a[i].get())
                b = float(self.entry_b[i].get())
                c = float(self.entry_c[i].get())
                self.equations.append((a, b, c))

            self.plot_quadratic_equations()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical coefficients")

    def generate_equation_fields(self):
        num = self.num_equations.get()

        for widget in self.frame_equations.winfo_children():
            widget.destroy()

        self.entry_a, self.entry_b, self.entry_c = [], [], []

        for i in range(num):
            label = tk.Label(self.frame_equations, text=f"Equation {i + 1}:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.E)

            entry_a = tk.Entry(self.frame_equations)
            entry_a.grid(row=i, column=1, padx=5, pady=5)
            self.entry_a.append(entry_a)

            entry_b = tk.Entry(self.frame_equations)
            entry_b.grid(row=i, column=2, padx=5, pady=5)
            self.entry_b.append(entry_b)

            entry_c = tk.Entry(self.frame_equations)
            entry_c.grid(row=i, column=3, padx=5, pady=5)
            self.entry_c.append(entry_c)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuadraticEquationPlotter(root)
    root.mainloop()
