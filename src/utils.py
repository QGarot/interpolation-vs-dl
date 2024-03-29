import numpy as np
from math import floor, ceil

def get_interpolation_set(f: callable, xj: list) -> list[tuple]:
    """
    Retourne les points d'interpolation (xj, f(xj))
    Paramètres :
    - f : fonction dont on souhaite déterminer les points d'interpolation associés aux xj
    - xj : tableau contenant les abscisses des points d'interpolation
    Retour : [(x1, f(x1)), (x2, f(x2)), ..., (xn, f(xn))]
    """
    yj = [f(x) for x in xj]
    return [(xj[j], yj[j]) for j in range(len(xj))]


def fact(n: int) -> int:
    """
    Fonction factorielle (en récursif)
    Paramètre :
    - n : entier pour lequel on souhaite calculer sa factorielle
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def inf_norm(f: callable, R: float) -> float:
    """
    Retourne la norme infinie de f sur l'intervalle [-R, R]
    Paramètre :
    - f : fonction à valeur réelle
    - R : rayon permettant de définir l'intervalle sur lequel on souhaite calculer la norme infinie
    Retour : ||f||_{inf, [-R, R]}
    """
    I = np.linspace(-R, R, ceil(R) * 50)
    img = []

    for x in I:
        img.append(abs(f(x)))

    return max(img)
