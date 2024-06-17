"""
Module principal : affichage des résultats principaux repris dans le rapport
"""

from functions import *
from neville_aitken import display_interpolation, get_xj
from serie import display_serie_expansion
from compare import inter_vs_serie

n = None # Ordre
R = None # Rayon de l'intervalle d'étude

# f0
print("f(x) = 1/(1+x^2)")
n = 11
R = 4
display_interpolation(f0, get_xj(n, R), R)
n = 45
R = 0.9
display_serie_expansion(f0, a0, n, R)
inter_vs_serie(f0, a0, 15, 0.90)

# f1
print("f(x) = 1/(1-x)")
n = 30
R = 0.9
display_interpolation(f1, get_xj(n, R), R)
n = 10
R = 0.90
display_serie_expansion(f1, a1, n, R)
inter_vs_serie(f1, a1, 15, 0.90)

# f2
print("f(x) = sin(x)")
n = 10
R = 4
display_interpolation(f2, get_xj(n, R), R)
n = 25
R = 10
display_serie_expansion(f2, a2, n, R)
inter_vs_serie(f2, a2, 20, 7)

# f3
print("f(x) = exp(x)")
n = 10
R = 3
display_interpolation(f3, get_xj(n, R), R)
n = 10
R = 6
display_serie_expansion(f3, a3, n, R)
inter_vs_serie(f3, a3, 8, 4)

# f6
print("f(x) = cos(x)exp(x)")
n = 7
R = 5
display_interpolation(f6, get_xj(n, R), R)
n = 16
R = 5
display_serie_expansion(f6, a6, n, R)
inter_vs_serie(f6, a6, 16, 5)
