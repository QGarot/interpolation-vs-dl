import numpy as np
import matplotlib.pyplot as plt
from math import floor

def display_test(f, devlim, R: float):
    n = floor(R * 20)
    pts = np.linspace(-R, R, n)

    # Affichage de la fonction
    fx = np.array([f(x) for x in pts])
    plt.plot(pts, fx, color="tab:blue", label="f")

    # Affichage du DL (en plusieurs points)
    devlims = np.array([devlim(25, x) for x in pts])
    plt.plot(pts, devlims, color="tab:green", linestyle="--", label="Approximation de f par son DL")

    plt.legend()
    plt.show()
