"""
Outil de comparaison des deux méthodes d'approximation polynomiale
"""

import numpy as np
from utils import inf_norm
from neville_aitken import get_xj, neville, get_interpolation_set
import matplotlib.pyplot as plt
from serie import horner


def inter_vs_serie(f: callable, a: callable, order: int, R: float, log: bool = False) -> None:
    """
    Compare les erreurs d'approximation
    Paramètres :
    - f : fonction étudiée
    - a : suite des coefficients du développement limité de la fonction f
    - order : ordre du Dl ET nombre de points d'interpolation
    - R : rayon permettant de définir l'intervalle d'étude
    Retour : None
    """
    # Ordres
    n = []

    # Erreurs d'approximation mesurées avec la norme infinie
    err_inter = []
    err_serie = []

    # Initialisation de la mesure de l'erreur pour chaque itération
    err = None

    # On regarde comment se comporte l'erreur lorsque l'ordre augmente
    for i in range(0, order + 1):
        n.append(i)

        # Interpolation
        xj = get_xj(i + 1, R)
        set = get_interpolation_set(f, xj)
        norm = inf_norm(lambda x: f(x) - neville(set, x), R)
        err_inter.append(norm)

        # DL
        coefs = [a(k) for k in range(0, i + 1)] # Peut être défini en dehors de la boucle principale pour éviter les calculs redondants
        norm = inf_norm(lambda x: f(x) - horner(coefs, x), R)
        err_serie.append(norm)

    if log:
        plt.plot(n, np.log10(err_inter), marker=".", linestyle=":", label="$\phi$")
        plt.plot(n, np.log10(err_serie), marker=".", linestyle=":", label="$\psi$")
    else:
        plt.plot(n, err_inter, marker=".", linestyle=":", label="$\phi$")
        plt.plot(n, err_serie, marker=".", linestyle=":", label="$\psi$")
        
    plt.legend()
    plt.show()
