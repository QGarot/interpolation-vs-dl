import numpy as np
from utils import inf_norm, get_interpolation_set
from neville_aitken import get_xj, neville
import matplotlib.pyplot as plt


def inter_vs_dl(f: callable, dl: callable, order: int, R: float) -> None:
    """
    Compare les erreurs d'approximation
    Paramètres :
    - f : fonction étudiée
    - dl : développement limité de la fonction f (dans l'intervalle de convergence....)
    - order : ordre du Dl ET nombre de points d'interpolation
    - R : rayon permettant de définir l'intervalle d'étude
    """
    # Ordres
    n = []

    # Erreurs d'approximation mesurées avec la norme infinie
    err_inter = []
    err_dl = []

    # Initialisation de la mesure de l'erreur pour chaque itération
    norm = None

    # On regarde comment se comporte l'erreur lorsque l'ordre augmente
    for i in range(1, order + 1):
        n.append(i)

        # Interpolation
        xj = get_xj(i, R)
        set = get_interpolation_set(f, xj)
        norm = inf_norm(lambda x: f(x) - neville(set, x), R)
        err_inter.append(norm)

        # DL
        norm = inf_norm(lambda x: f(x) - dl(i, x), R)
        err_dl.append(norm)

    plt.plot(n, err_inter, label="Erreur d'interpolation")
    plt.plot(n, err_dl, label="Erreur DL")
    plt.legend()
    plt.show()
