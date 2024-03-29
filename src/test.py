from neville_aitken import neville, display_interpolation, get_xj, error
from math import log, exp
from dl import display_test
from functions import *
from compare import inter_vs_dl

# f(x) = x²+1 ; (0,1), (3, 10)
# print(neville([(0, 1), (3, 10), (5, 26)], 7))

# g = lambda x: -log(x**2 + 1)+4
#pts = [-5, -4.5, -3.3, -2, -1.5, 0.6, 0, 1.5, 3.5, 4, 5]

# h = lambda x: 1/(1 - x)
#pts = [-0.70, -0.60, -0.30, 0, 0.4, 0.8]

# erreur
inter_vs_dl(f1, dl_f1, 50, 0.70)

# f0 - Runge
print("- f(x) = 1/(1+x**2)")
pts_tcheby = get_xj(60, 6)
display_interpolation(f0, pts_tcheby, 6)
display_test(f0, dl_f0, 0.97)

# f1
print("- f(x) = 1/(1-x)")
pts_tcheby = get_xj(10, 6)
display_interpolation(f1, pts_tcheby, 6)
display_test(f1, dl_f1, 0.97)

# f2
print("- f(x) = cos(x)")
pts_tcheby = get_xj(10, 10)
display_interpolation(f2, pts_tcheby, 10)
display_test(f2, dl_f2, 10)

# f4
print("- f(x) = -log(x**2 + 1) + 4")
pts_tcheby = get_xj(5, 5)
display_interpolation(f4, pts_tcheby, 5)

# f5
print("- f(x) = exp(x)")
pts_tcheby = get_xj(5, 4)
display_interpolation(f5, pts_tcheby, 4)
display_test(f5, dl_f5, 4)
