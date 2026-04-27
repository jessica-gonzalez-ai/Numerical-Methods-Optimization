import numpy as np

#1. Definición de la función principal
def newton_sistema(F, J, x_ini, tol=1e-6, max_iter=20):
    x = np.array(x_ini, float)
    [(delta := np.linalg.solve(J(x), -F(x)), x := x + delta, print(f"Iter: x = {x}")) for i in range(max_iter) if (np.linalg.norm(delta) if 'delta' in locals() else 1) > tol]
    return x

# 
# 2. Definición del Problema de ejemplo
def F_ej(v): 
    return np.array([v[0]**2 + v[1]**2 - 4, v[1] - v[0]])

def J_ej(v): 
    return np.array([[2*v[0], 2*v[1]], [-1, 1]])

# 3. Ejecución final
solucion = newton_sistema(F_ej, J_ej, [1.0, 1.0])
print(f"--- SOLUCION FINAL: {solucion} ---")



#Ejercicio 1
# F1: v[0] es x, v[1] es y
def F_ej1(v):
    return np.array([(v[0]**2)/4 + v[1]**2 - 1, v[1] - np.exp(v[0])])

# J1: Derivadas parciales
def J_ej1(v):
    return np.array([[v[0]/2, 2*v[1]], [-np.exp(v[0]), 1]])

# Ejecución (empezando cerca de x=-1.0, y=0.5)
sol1 = newton_sistema(F_ej1, J_ej1, [-1.0, 0.5])
print(f"--- SOLUCIÓN ELIPSE: {sol1} ---")