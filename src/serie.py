"""
Contient les fonctions relatives à la méthode d'approximation par DL/séries entières
"""

import numpy as np
import matplotlib.pyplot as plt
from math import floor


def horner(a: list, x: float) -> float:
    """
    Evalue le polynôme P dont les coefficients sont stockés dans la liste donnée en x
    Paramètres :
    - a : liste des coefficients du polynôme
    - x : valeur d'évaluation
    Retour : P(x)
    """
    n = len(a)
    r = a[n-1]
    for i in range(n - 2, -1, -1):
        r = r * x + a[i]
    return r

def display_serie_expansion(f: callable, a: callable, n: int, R: float) -> None:
    """
    Affiche la fonction f et son approximation par développement limité à l'ordre donné
    Paramètres :
    - f : fonction étudiée
    - a: coefficient du développement limité / de la série entière.
         Exemple: pour la fonction exponentielle, a(n) = 1/n!.
    - n : ordre
    - R : rayon de l'intervalle sur lequel on souhaite reprensenter les résultats
    Retour : None
    """
    m = floor(R * 100) # nombre de points
    pts = np.linspace(-R, R, m)

    # Affichage de la fonction f
    fx = np.array([f(x) for x in pts])
    plt.plot(pts, fx, color="tab:blue", label="$f(x)$")

    # Affichage du DL
    coefs = [a(k) for k in range(0, n + 1)]
    y = np.array([horner(coefs, x) for x in pts])
    plt.plot(pts, y, color="tab:green", linestyle="--", label="DL")

    plt.legend(loc="upper right")
    plt.show()
