def secante(f, x0, x1, tol=1e-6, max_iter=50):
    for i in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1 - fx0) < 1e-12: break
        x_n = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        print("Iteracion {0}: x = {1:.8f}".format(i+1, x_n))
        if abs(x_n - x1) < tol: return x_n
        x0, x1 = x1, x_n
    return x1

import math

# Caso 1: Ejemplo inicial
f_ej = lambda x: math.exp(-x) - x
resultado = secante(f_ej, 0, 1)
print("Resultado final: {0:.8f}\n".format(resultado))

# Caso 2: Hallar raíz de 3
f_ej2 = lambda x: x**2 - 3
resultado2 = secante(f_ej2, 1, 2)
print("Resultado final: {0:.8f}\n".format(resultado2))

# Caso 3: Raíz de Polinomio
f_ej3 = lambda x: x**3 - x - 1
resultado3 = secante(f_ej3, 1, 2)
print("Resultado final: {0:.8f}\n".format(resultado3))

# Caso 4: Función Trigonométrica
f_ej4 = lambda x: math.cos(x) - x
resultado4 = secante(f_ej4, 0, 1)
print("Resultado final: {0:.8f}".format(resultado4))