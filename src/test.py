"""
Fichier d'essais
"""

import numpy as np
from neville_aitken import display_interpolation, neville, get_xj
from functions import *

# Vérification du bon fonctionnement de la méthode de Neville :
# f(x) = x^2+1, noeuds (0,1), (3, 10) et (5, 26)
# En renseignant 3 noeuds, on aura une interpolation d'ordre 2 et l'interpolant sera la fonction f
print("# Vérification du bon fonctionnement de la méthode de Neville")
print(neville([(0, 1), (3, 10), (5, 26)], 7)) # retourne bien 50


# f0 - Runge avec points d'interpolation équi-répartis
print("- f(x) = 1/(1+x**2)")
n = 13
R = 5
pts_tcheby = np.linspace(-R, R, n)
display_interpolation(f0, pts_tcheby, R)

# f8
print("f(x) = -log(x**2 + 1) + x")
n = 20
R = 10
display_interpolation(f8, get_xj(n, R), R)

# f9, (fonction qui, par les théorèmes de prolongement, est bien de classe C infini)
print("f(x) = exp(-1 / x) if x > 0 else 0")
n = 20
R = 6
display_interpolation(f9, get_xj(n, R), R)
