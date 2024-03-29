import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi, floor
from utils import inf_norm, get_interpolation_set

def neville(set: list[tuple], x: float) -> float:
    """
    Paramètres :
    - set : liste contenant les points d'interpolations
    - x : valeur en laquelle on cherche à évaluer le polynôme interpolateur
    Retour : le polynôme interpolateur évalué en x selon le schéma de Neville-Aitken
    """

    n = len(set) - 1
    p = np.zeros((n + 1, n + 1))

    # Initialisation :
    # Quelque soit i, le pol. de degré 0 passant par (x_i, y_i) est le pol. constant y_i
    p[:,0] = [set[i][1] for i in range(n + 1)]

    # Itérations (en respectant l'ordre de calcul)
    for k in range(1, n + 1):
        for i in range(0, n + 1 - k):
            p[i, k] = ((set[i + k][0] - x) * p[i, k - 1] - (set[i][0] - x) * p[i + 1, k - 1]) / (set[i + k][0] - set[i][0])

    return p[0, n]
        
def display_interpolation(f: callable, xj: list, R: float) -> None:
    """
    Affiche un graphe représentant la fonction f et son interpolation polynomiale
    Paramètres :
    - f : la fonction que l'on cherche à interpoler
    - xj : liste contenant les points (abscisse) d'interpolation
    - R : rayon de l'intervalle sur lequel on souhaite reprensenter les résultats
    Retour : None
    """
    n = floor(R) * 20
    pts = np.linspace(-R, R, n)

    # Initialisation et affichage des points d'interpolation
    #yj = [f(x) for x in xj]
    set = get_interpolation_set(f, xj)
    #plt.plot(xj, yj, color="tab:orange", marker="o", linestyle="", label="Points d'interpolation")

    # Affichage de la fonction
    fx = np.array([f(x) for x in pts])
    plt.plot(pts, fx, color="tab:blue", label="f")

    # Affichage du polynôme d'interpolation
    p = np.array([neville(set, x) for x in pts])
    plt.plot(pts, p, color="tab:green", linestyle="--", label="Interpolation polynomiale de f")

    plt.legend()
    plt.show()

def get_xj(n: int, R: float = 1) -> list:
    """
    Retourne les points (xj) dans l'intervalle [-R, R] pour avoir la meilleure interpolation
    Paramètre :
    - n : nombre de points souhaités
    - R : rayon de l'intervalle dans lequel les points doivent être choisis
    Retour : une liste de points
    """
    return [cos((2*i + 1) * pi / (2*n + 2)) * R for i in range(n + 1)]

def error(f: callable, tests: int, R: float) -> None:
    """
    Graphe de l'erreur en fonction du nombre de points d'interpolation
    Paramètres :
    - f : fonction étudiée
    - tests : nombre de tests à affectuer
    - R : rayon permettant de définir l'intervalle sur lequel on fait l'étude
    """
    n = []
    err = []
    norm = None
    for i in range(1, tests + 1):
        n.append(i)

        # Jeu de points
        xj = get_xj(i, R)
        yj = [f(x) for x in xj]
        set = [(xj[j], yj[j]) for j in range(len(xj))]

        norm = inf_norm(lambda x: f(x) - neville(set, x), R)
        err.append(norm)

    plt.plot(n, err)
    plt.title("Graphe de $||f-Pnf||_{\infty}$")
    plt.xlabel("$n$ entier naturel")
    plt.ylabel("$||f-Pnf||_{\infty}$")
    plt.show()
