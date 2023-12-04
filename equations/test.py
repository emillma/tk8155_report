import sympy as sp
from sympy import latex
import pyperclip




def lprint(*things):
    
    print(latex(*things))
    
a,b,c = sp.symbols('a,b,c')
#bold x
img_gt_i = sp.symbols(r"I_i")
img_est_i = sp.symbols(r"\hat{I}_i")

renrender = sp.symbols(r'\mathbf{R}')
x = sp.symbols(r'\mathbf{x}_a')
s = sp.Sum(x,(a,1,b))


lprint(s)
lprint(img_gt_i)
lprint(img_est_i)