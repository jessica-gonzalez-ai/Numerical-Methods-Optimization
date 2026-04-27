
import math
import numpy as np
import matplotlib.pyplot as plt

#1.Función
def f(c):
    return (9.8 * 68.1 / c) * (1 - math.exp(-(c / 68.1) * 10)) - 40

#2.Intervalo
a = 12
b = 16

#3.f(a) y f(b)
fa = f(a)
fb = f(b)

#4.Cambio de signo
print("--- Justificación de Cambio de Signo ---")
print(f"f({a}) = {fa:.4f}")
print(f"f({b}) = {fb:.4f}")
print(f"Multiplicación f(a) * f(b) = {fa * fb:.4f}")

if fa * fb < 0:
    print("Resultado: ¡Justificación correcta! Hay un cambio de signo.")
else:
    print("Resultado: No hay cambio de signo, revisa el intervalo.")


#5.(Bisección
tolerancia = 1e-6
iteracion = 1

print("\n--- Paso 2: Tabla de Iteraciones (Método de Bisección) ---")
print(f"{'Iter':<6} | {'a':<10} | {'b':<10} | {'c (Punto medio)':<15} | {'f(c)':<15}")
print("-" * 65)

#6.While
while abs(b - a) > tolerancia:
    # Calcular el punto medio
    c = (a + b) / 2
    fc = f(c)
    
    #Imprimir la fila actual
    print(f"{iteracion:<6} | {a:<10.5f} | {b:<10.5f} | {c:<15.5f} | {fc:<15.5f}")

    if fa * fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc
        
    iteracion += 1
    #Max.100
    if iteracion > 100:
        break

#7.Resultado Finaaal
raiz_aproximada = (a + b) / 2
print("-" * 65)
print(f"\n¡Listo! El método convergió.")
print(f"Raíz aproximada = {raiz_aproximada:.6f}")

#8.Gráfica
print("\n--- Paso 3: Generando Gráfica ---")
x = np.linspace(1, 100, 1000)
y = [f(val) for val in x]

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(c)', color='blue')

#línea horizontal en y=0 
plt.axhline(0, color='black', linewidth=1, linestyle='--')

#punto
plt.plot(raiz_aproximada, f(raiz_aproximada), 'ro', label=f'Raíz aprox: {raiz_aproximada:.4f}')

#modificaciones de la gráfica
plt.xlabel("c (Coeficiente)")
plt.ylabel("f(c)")
plt.title("Gráfica de la función y su raíz")
plt.grid(True)
plt.legend()
plt.show()