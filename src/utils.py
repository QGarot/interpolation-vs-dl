"""
Quelques fonctions utiles pour le reste du programme
"""

import numpy as np
from math import floor, ceil


def fact(n: int) -> int:
    """
    Fonction factorielle (en récursif)
    Paramètre :
    - n : entier pour lequel on souhaite calculer sa factorielle
    Retour : n!
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
    I = np.linspace(-R, R, ceil(R) * 150)
    img = []

    for x in I:
        img.append(abs(f(x)))

    return max(img)
