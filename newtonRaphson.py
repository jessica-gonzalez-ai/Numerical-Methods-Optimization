def newton_raphson(f, df, x0, tol=1e-6, max_iter=50):
    x = x0
    for i in range(max_iter):
        dfx = df(x)
        if abs(dfx) < 1e-12: break
        x_nuevo = x - f(x) / dfx
        print("Iteracion {0}: x = {1:.8f}".format(i+1, x_nuevo))
        if abs(x_nuevo - x) < tol: return x_nuevo
        x = x_nuevo
    return x

import math

# Caso 1: Ejemplo inicial
f = lambda x: x**2 - 2
df = lambda x: 2*x
resultado = newton_raphson(f, df, 1.5)
print("Resultado final: {0:.8f}\n".format(resultado))

# Ejercicio 1: Raíz cúbica de 10
f1 = lambda x: x**3 - 10
df1 = lambda x: 3*x**2
resultado1 = newton_raphson(f1, df1, 2)
print("Resultado final: {0:.8f}\n".format(resultado1))

# Ejercicio 2: Coseno
f2 = lambda x: math.cos(x) - x
df2 = lambda x: -math.sin(x) - 1
resultado2 = newton_raphson(f2, df2, 0.5)
print("Resultado final: {0:.8f}".format(resultado2))