"""
Contient toutes les fonctions étudiées
- fi : i-ème fonction
- ai : suite des coefficients du développement limité / de la série entière
       (sous réserve d'existence) de la i-ème fonction
"""

from math import cos, sin, log, exp, pi
from utils import fact


f0 = lambda x: 1 / (1 + x**2) # Runge
a0 = lambda n: (-1)**(n / 2) if n % 2 == 0 else 0

f1 = lambda x: 1 / (1 - x)
a1 = lambda n: 1

f2 = lambda x: sin(x)
a2 = lambda n: (-1)**((n - 1) / 2) / fact(n) if n % 2 == 1 else 0

f3 = lambda x: exp(x)
a3 = lambda n: 1 / fact(n)

f4 = lambda x: log(1 + x)
a4 = lambda n: (-1)**(n + 1) / n  if n != 0 else 0

f5 = lambda x: 1 / (1 + x)
a5 = lambda n: (-1)**n

f6 = lambda x: cos(x) * exp(x)
a6 = lambda n: (2**(n / 2) * cos(n * pi / 4)) / fact(n)

f7 = lambda x: exp(-x) * (cos(x) + sin(x))
a7 = lambda n: (2**(n / 2) * cos(n * pi / 4)) / fact(n)

f8 = lambda x: -log(x**2 + 1) + x
f9 = lambda x: exp(-1 / x) if x > 0 else 0
