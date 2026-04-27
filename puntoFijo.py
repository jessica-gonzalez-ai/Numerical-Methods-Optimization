def punto_fijo(g, x0, tol=1e-6, max_iter=30):
    x = x0
    [print(f"Iter {i+1}: x={(x:=g(x)):.8f}") for i in range(max_iter)]
    return x

import math

# Caso inicial
g_ej = lambda x: math.cos(x)
resultado = punto_fijo(g_ej, 0.5)
print(f"--- RESULTADO FINAL: {resultado:.8f} ---\n")

# Ejercicio 1: Raíz de 3 (Convergente)
g_ej1 = lambda x: (x + 3/x) / 2
resultado1 = punto_fijo(g_ej1, 1.0)
print(f"--- RESULTADO Ejercicio 1: {resultado1:.8f} ---\n")

# Ejercicio 2: Oscilación (Divergente)
g_ej2 = lambda x: 3 / x
resultado2 = punto_fijo(g_ej2, 1.5)
print(f"--- RESULTADO Ejercicio 2: {resultado2:.8f} ---")