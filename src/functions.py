from math import cos, sin, log, exp
from utils import fact


f0 = lambda x: 1/(1+x**2) # runge
f1 = lambda x: 1/(1-x)
f2 = lambda x: cos(x)
f3 = lambda x: sin(x)
f4 = lambda x: -log(x**2 + 1) + 4
f5 = lambda x: exp(x)

# TODO: gagner en complexité en utilisant l'algorithme de Horner par exemple

def dl_f0(order: int, x: float) -> float:
    """
    Evaluation naïve en x de la partie régulière du DL de f0 à l'ordre donné
    Paramètres :
    - order : ordre du DL
    - x : valeur d'évaluation
    Retour : float
    """
    s = 0
    for n in range(order + 1):
        s = s + (-1)**n * x ** (2*n)
    return s

def dl_f1(order: int, x: float) -> float:
    """
    Evaluation naïve en x de la partie régulière du DL de f0 à l'ordre donné
    Paramètres :
    - order : ordre du DL
    - x : valeur d'évaluation
    Retour : float
    """
    s = 0
    for n in range(order + 1):
        s = s + x ** (n)
    return s

def dl_f2(order: int, x: float) -> float:
    """
    Evaluation naïve en x de la partie régulière du DL de f0 à l'ordre donné
    Paramètres :
    - order : ordre du DL
    - x : valeur d'évaluation
    Retour : float
    """
    s = 0
    for n in range(order + 1):
        s = s + (-1)**n * (x ** (2*n)) / fact(2*n)
    return s

def dl_f5(order: int, x: float) -> float:
    """
    Evaluation naïve en x de la partie régulière du DL de f0 à l'ordre donné
    Paramètres :
    - order : ordre du DL
    - x : valeur d'évaluation
    Retour : float
    """
    s = 0
    for n in range(order + 1):
        s = s + 1/fact(n) * x**n
    return s
