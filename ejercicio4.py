import numpy as np
import matplotlib.pyplot as plt

#1.Función
def f(x):
    return x**3 - 4*x - 9

# 2.Intervalo
a = 2.0
b = 3.0

#3. Calculamos f(a) y f(b)
fa = f(a)
fb = f(b)

#4. Verificamos el cambio de signo
print("--- Justificación de Cambio de Signo ---")
print(f"f({a}) = {fa:.4f}")
print(f"f({b}) = {fb:.4f}")
print(f"Multiplicación f(a) * f(b) = {fa * fb:.4f}")

if fa * fb < 0:
    print("Resultado: ¡Justificación correcta! Hay un cambio de signo.")
else:
    print("Resultado: No hay cambio de signo, revisa el intervalo.")

#5.Bisección
tolerancia = 1e-6
iteracion = 1

print("\n--- Paso 2: Tabla de Iteraciones (Método de Bisección) ---")
print(f"{'Iter':<6} | {'a':<10} | {'b':<10} | {'x (Punto medio)':<15} | {'f(x)':<15}")
print("-" * 65)

#6. Ciclo while
while abs(b - a) > tolerancia:
    c = (a + b) / 2
    fc = f(c)
    
    print(f"{iteracion:<6} | {a:<10.5f} | {b:<10.5f} | {c:<15.5f} | {fc:<15.5f}")
    
    if fa * fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc
        
    iteracion += 1
    if iteracion > 100:
        break

#7. Resultado final
raiz_aproximada = (a + b) / 2
print("-" * 65)
print(f"\n¡Listo! El método convergió.")
print(f"Raíz aproximada = {raiz_aproximada:.6f}")

#8.Gráfica
print("\n--- Paso 3: Generando Gráfica ---")
x_vals = np.linspace(1, 4, 500)
y_vals = [f(val) for val in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='f(x) = x^3 - 4x - 9', color='teal')
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.plot(raiz_aproximada, f(raiz_aproximada), 'ro', label=f'Raíz aprox: {raiz_aproximada:.4f}')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica de f(x) = x^3 - 4x - 9")
plt.grid(True)
plt.legend()
plt.show()