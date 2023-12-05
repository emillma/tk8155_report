from matplotlib import pyplot as plt
import numpy as np

"""
x-0.5
x+0.5

"""
def gauss(x):
    return np.exp(-(3*x)**2)

def poly1(x):
    return 1-x**2

def poly2(x):
    return (1-x**2)**2

def poly4(x):
    return (x**2-1)**4

def polyd(x):
    return (1-x**2)**2 * (1+x**2)

def combind(fa, fb, fk):
    return lambda x: fa(x) * fk(x) + fb(x) * (1-fk(x))


f = combind(poly1, poly4, poly4)

t = np.linspace(-1.0, 1.0, 1000)
plt.plot(t, gauss(t), label='$e^{-(3x)^2}$')
plt.plot(t, poly1(t), label='$1-x^2$')
plt.plot(t, poly2(t), label='$1-x^2)^2$')
# plt.plot(t, poly4(t), label='$(1-x^2)^4$')
# plt.plot(t, polyd(t), label='$(1-x^2)^2(1+x^2)$')
# plt.plot(t, polyd(t), label='$(1-x^2)^2(1+x^2)$')
plt.legend()
plt.show()