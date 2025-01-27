import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm, assoc_laguerre  # Spherical harmonics and Laguerre polynomials
from mpl_toolkits.mplot3d import Axes3D

# Constants
a0 = 1.0  # Bohr radius (in atomic units)
Z = 1  # Atomic number (hydrogen)


# Define a grid in spherical coordinates
def spherical_grid(r_max, n_points):
    r = np.linspace(0, r_max, n_points)
    theta = np.linspace(0, np.pi, n_points)
    phi = np.linspace(0, 2 * np.pi, n_points)
    r, theta, phi = np.meshgrid(r, theta, phi, indexing='ij')
    return r, theta, phi


# Convert spherical to Cartesian coordinates
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z


# Full radial wavefunction for hydrogen
def radial_wavefunction(n, l, r):
    # Prefactor
    prefactor = np.sqrt((2 * Z / (n * a0)) ** 3 * np.math.factorial(n - l - 1) / (2 * n * np.math.factorial(n + l)))
    # Exponential term
    exponential = np.exp(-Z * r / (n * a0))
    # Power term
    power = (2 * Z * r / (n * a0)) ** l
    # Associated Laguerre polynomial
    laguerre = assoc_laguerre(2 * Z * r / (n * a0), n - l - 1, 2 * l + 1)
    # Combine all terms
    R = prefactor * exponential * power * laguerre
    return R


# Probability density of an orbital
def orbital_density(n, l, m, r, theta, phi):
    # Radial part (full wavefunction)
    R = radial_wavefunction(n, l, r)
    # Angular part (spherical harmonics)
    Y = sph_harm(m, l, phi, theta)
    # Wavefunction
    psi = R * Y
    # Probability density
    density = np.abs(psi) ** 2
    # Normalize density
    density /= np.max(density)
    return psi, density  # Return both psi and density


# Plot a single orbital with custom transparency and color
def plot_orbital(n, l, m, r_max, n_points=100, alpha=1.0, title=None):
    r, theta, phi = spherical_grid(r_max, n_points)
    x, y, z = spherical_to_cartesian(r, theta, phi)
    psi, density = orbital_density(n, l, m, r, theta, phi)

    # Create a 3D plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # For orbitals with lobes, split into positive and negative regions
    if l > 0:
        positive_lobe = psi > 0  # Positive values of the wavefunction
        negative_lobe = psi < 0  # Negative values of the wavefunction

        # Plot the positive lobe in red
        ax.scatter(x[positive_lobe], y[positive_lobe], z[positive_lobe],
                   c=density[positive_lobe], cmap='Reds', s=2, alpha=alpha, label="Positive Lobe")

        # Plot the negative lobe in blue
        ax.scatter(x[negative_lobe], y[negative_lobe], z[negative_lobe],
                   c=density[negative_lobe], cmap='Blues', s=2, alpha=alpha, label="Negative Lobe")
    else:
        # For s orbitals, plot the entire density
        ax.scatter(x, y, z, c=density.ravel(), cmap='viridis', s=2, alpha=alpha)

    ax.set_title(title if title else f"Orbital: n={n}, l={l}, m={m}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio
    if l > 0:
        ax.legend()
    plt.show()


# Plot a 2D cross-section of the orbital
def plot_cross_section(n, l, m, r_max, n_points=100, title=None):
    # Create a 2D grid in the x-z plane (y = 0)
    x = np.linspace(-r_max, r_max, n_points)
    z = np.linspace(-r_max, r_max, n_points)
    x, z = np.meshgrid(x, z)
    y = np.zeros_like(x)  # Set y = 0 for the x-z plane

    # Convert Cartesian to spherical coordinates
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)

    # Calculate the wavefunction and density
    psi, density = orbital_density(n, l, m, r, theta, phi)

    # Create a 2D plot
    plt.figure(figsize=(8, 8))
    plt.contourf(x, z, density, levels=50, cmap='viridis')
    plt.colorbar(label='Probability Density')
    plt.title(title if title else f"Cross-Section: n={n}, l={l}, m={m}")
    plt.xlabel('X')
    plt.ylabel('Z')
    plt.show()

# Example usage
def draw_all():
    orbitals = [
        (1, 0, 0, "1s"),
        (2, 0, 0, "2s"),
        (2, 1, -1, "2px"),
        (2, 1, 0, "2pz"),
        (2, 1, 1, "2py"),
        (3, 0, 0, "3s"),
        (3, 1, -1, "3px"),
        (3, 1, 0, "3pz"),
        (3, 1, 1, "3py"),
        (3, 2, -2, "3dxy"),
        (3, 2, -1, "3dyz"),
        (3, 2, 0, "3dz^2"),
        (3, 2, 1, "3dxz"),
        (3, 2, 2, "3dx^2-y^2"),
        (4, 0, 0, "4s"),
        (4, 1, -1, "4px"),
        (4, 1, 0, "4pz"),
        (4, 1, 1, "4py"),
        (4, 2, -2, "4dxy"),
        (4, 2, -1, "4dyz"),
        (4, 2, 0, "4dz^2"),
        (4, 2, 1, "4dxz"),
        (4, 2, 2, "4dx^2-y^2"),
        (4, 3, -3, "4f(x^3 - 3xy^2)"),
        (4, 3, -2, "4fxyz"),
        (4, 3, -1, "4fz(x^2 - y^2)"),
        (4, 3, 0, "4fz^3"),
        (4, 3, 1, "4fz^2x"),
        (4, 3, 2, "4fyz^2"),
        (4, 3, 3, "4fxz^2"),
        (5, 0, 0, "5s"),
        (5, 1, -1, "5px"),
        (5, 1, 0, "5pz"),
        (5, 1, 1, "5py"),
        (5, 2, -2, "5dxy"),
        (5, 2, -1, "5dyz"),
        (5, 2, 0, "5dz^2"),
        (5, 2, 1, "5dxz"),
        (5, 2, 2, "5dx^2-y^2"),
        (5, 3, -3, "5f(x^3 - 3xy^2)"),
        (5, 3, -2, "5fxyz"),
        (5, 3, -1, "5fz(x^2 - y^2)"),
        (5, 3, 0, "5fz^3"),
        (5, 3, 1, "5fz^2x"),
        (5, 3, 2, "5fyz^2"),
        (5, 3, 3, "5fxz^2"),
        (5, 4, -4, "5g(x^4 - 6x^2y^2 + y^4)"),
        (5, 4, -3, "5gx(x^2 - 3y^2)"),
        (5, 4, -2, "5gxyz"),
        (5, 4, -1, "5gz(x^2 - y^2)"),
        (5, 4, 0, "5gz^4"),
        (5, 4, 1, "5gz^3x"),
        (5, 4, 2, "5gz^2(x^2 - y^2)"),
        (5, 4, 3, "5gz(x^3 - 3xy^2)"),
        (5, 4, 4, "5g(x^3 - 3xy^2)"),
        (6, 0, 0, "6s"),
        (6, 1, -1, "6px"),
        (6, 1, 0, "6pz"),
        (6, 1, 1, "6py"),
        (6, 2, -2, "6dxy"),
        (6, 2, -1, "6dyz"),
        (6, 2, 0, "6dz^2"),
        (6, 2, 1, "6dxz"),
        (6, 2, 2, "6dx^2-y^2"),
        (6, 3, -3, "6f(x^3 - 3xy^2)"),
        (6, 3, -2, "6fxyz"),
        (6, 3, -1, "6fz(x^2 - y^2)"),
        (6, 3, 0, "6fz^3"),
        (6, 3, 1, "6fz^2x"),
        (6, 3, 2, "6fyz^2"),
        (6, 3, 3, "6fxz^2"),
        (6, 4, -4, "6g(x^4 - 6x^2y^2 + y^4)"),
        (6, 4, -3, "6gx(x^2 - 3y^2)"),
        (6, 4, -2, "6gxyz"),
        (6, 4, -1, "6gz(x^2 - y^2)"),
        (6, 4, 0, "6gz^4"),
        (6, 4, 1, "6gz^3x"),
        (6, 4, 2, "6gz^2(x^2 - y^2)"),
        (6, 4, 3, "6gz(x^3 - 3xy^2)"),
        (6, 4, 4, "6g(x^3 - 3xy^2)"),
        (6, 5, -5, "6h(x^5 - 10x^3y^2 + 5xy^4)"),
        (6, 5, -4, "6hx(x^4 - 6x^2y^2 + y^4)"),
        (6, 5, -3, "6hxyz(x^2 - y^2)"),
        (6, 5, -2, "6hz^2(x^2 - y^2)"),
        (6, 5, -1, "6hz^3x"),
        (6, 5, 0, "6hz^5"),
        (6, 5, 1, "6hz^3y"),
        (6, 5, 2, "6hz^2y^2"),
        (6, 5, 3, "6hxyz(x^2 - y^2)"),
        (6, 5, 4, "6hx(x^4 - 6y^2x^2 + y^4)"),
        (6, 5, 5, "6h(y^5 - 10y^3x^2 + 5x^4y)"),
        (7, 0, 0, "7s"),
        (7, 1, -1, "7px"),
        (7, 1, 0, "7pz"),
        (7, 1, 1, "7py"),
        (7, 2, -2, "7dxy"),
        (7, 2, -1, "7dyz"),
        (7, 2, 0, "7dz^2"),
        (7, 2, 1, "7dxz"),
        (7, 2, 2, "7dx^2-y^2"),
        (7, 3, -3, "7f(x^3 - 3xy^2)"),
        (7, 3, -2, "7fxyz"),
        (7, 3, -1, "7fz^2x"),
        (7, 3, 0, "7fz^3"),
        (7, 3, 1, "7fz^2y"),
        (7, 3, 2, "7fyz^2"),
        (7, 3, 3, "7f(x^3 - 3yx^2)"),
        (7, 4, -4, "7g(x^4 - 6x^2y^2 + y^4)"),
        (7, 4, -3, "7gx(x^3 - 3xy^2)"),
        (7, 4, -2, "7gxyz"),
        (7, 4, -1, "7gz^2x"),
        (7, 4, 0, "7gz^4"),
        (7, 4, 1, "7gz^2y"),
        (7, 4, 2, "7gyz^2"),
        (7, 4, 3, "7gy(x^3 - 3xy^2)"),
        (7, 4, 4, "7g(x^4 - 6yx^2 + y^4)"),
        (7, 5, -5, "7h(x^5 - 10x^3y^2 + 5xy^4)"),
        (7, 5, -4, "7hx(x^4 - 6x^2y^2 + y^4)"),
        (7, 5, -3, "7hxyz(x^2 - y^2)"),
        (7, 5, -2, "7hz^2(x^2 - y^2)"),
        (7, 5, -1, "7hz^3x"),
        (7, 5, 0, "7hz^5"),
        (7, 5, 1, "7hz^3y"),
        (7, 5, 2, "7hz^2y^2"),
        (7, 5, 3, "7hxyz(x^2 - y^2)"),
        (7, 5, 4, "7hx(x^4 - 6y^2x^2 + y^4)"),
        (7, 5, 5, "7h(y^5 - 10y^3x^2 + 5x^4y)")
    ]

    for n, l, m, orbital_name in orbitals:
        r_max = 8 * n ** 1.2  # Scale radial grid by n
        #plot_orbital(n, l, m, r_max=r_max, alpha=0.8, title=f"{orbital_name} Orbital (n={n}, l={l}, m={m})")
        plot_cross_section(n, l, m, r_max=r_max, title=f"{orbital_name} Orbital Cross-Section (n={n}, l={l}, m={m})")


# Initialize the Tkinter window
def create_ui():
    window = tk.Tk()
    window.title("Quantum Orbital Selector")

    # Function to get valid l values based on n
    def get_valid_l_values(n_value):
        """Return valid l values for the selected n value."""
        return list(range(n_value))  # l ranges from 0 to n-1

    # Function to get valid m values based on l
    def get_valid_m_values(l_value):
        """Return valid m values for the selected l value."""
        return list(range(-l_value, l_value + 1))  # m ranges from -l to +l

    # Function to update l options when n changes
    def update_l_options(*args):
        try:
            n_value = int(n_entry.get())
            if n_value <= 0:
                raise ValueError("Principal Quantum Number (n) must be greater than 0.")
            valid_l_values = get_valid_l_values(n_value)
            l_combobox['values'] = valid_l_values
            l_combobox.current(0)  # Set default to first valid l value
            update_m_options()  # Update m options based on new l value
        except ValueError:
            n_entry.delete(0, tk.END)
            n_entry.insert(0, "1")  # Reset to default valid value
            update_l_options()

    # Function to update m options when l changes
    def update_m_options(*args):
        try:
            l_value = int(l_combobox.get())
            valid_m_values = get_valid_m_values(l_value)
            m_combobox['values'] = valid_m_values
            m_combobox.current(0)  # Set default to first valid m value
        except ValueError:
            pass

    # Set up labels and entry fields for n, l, m
    tk.Label(window, text="Principal Quantum Number (n)").grid(row=0, column=0)
    tk.Label(window, text="Azimuthal Quantum Number (l)").grid(row=1, column=0)
    tk.Label(window, text="Magnetic Quantum Number (m)").grid(row=2, column=0)

    # n as an integer with input validation for greater than 0
    n_entry = ttk.Entry(window)
    n_entry.grid(row=0, column=1)
    n_entry.insert(0, "1")  # Default value for n
    n_entry.bind("<FocusOut>", update_l_options)  # Update l options when n changes

    # l as a dropdown (combobox)
    l_combobox = ttk.Combobox(window, state="readonly")
    l_combobox.grid(row=1, column=1)
    l_combobox.bind("<<ComboboxSelected>>", update_m_options)  # Update m options when l changes

    # m as a dropdown (combobox)
    m_combobox = ttk.Combobox(window, state="readonly")
    m_combobox.grid(row=2, column=1)

    # Initialize l and m options based on default n value
    update_l_options()

    # Function to handle plot button click
    def on_plot_button_click():
        n = int(n_entry.get())
        l = int(l_combobox.get())
        m = int(m_combobox.get())
        r_max = 8 * n ** 1.1  # Scale radial grid by n, numbers are sub-optimal, just to plot higher n in better way
        plot_cross_section(n, l, m, r_max=r_max, title=f" Orbital Cross-Section (n={n}, l={l}, m={m})")

    plot_button = ttk.Button(window, text="Cross section", command=on_plot_button_click)
    plot_button.grid(row=3, column=0, columnspan=2)

    # Run the UI window
    window.mainloop()

if __name__ == "__main__":
    create_ui()