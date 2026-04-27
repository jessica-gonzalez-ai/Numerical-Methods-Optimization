import numpy as np
import matplotlib.pyplot as plt

#1.Función del problema 5.2
def f(x):
    return 5 * x**3 - 5 * x**2 + 6 * x - 2

#2.IntervaloS
a = 0.0
b = 1.0

#3.Cambio de signo
fa = f(a)
fb = f(b)
print("--- Justificación de Cambio de Signo ---")
print(f"f({a}) = {fa:.4f}")
print(f"f({b}) = {fb:.4f}")

if fa * fb < 0:
    print("Resultado: ¡Correcto! Hay cambio de signo.")
else:
    print("Resultado: ERROR, revisa el intervalo.")

#4.Bisección con Error Porcentual
meta_error = 10.0 # Queremos bajar del 10%
error_actual = 100.0 # Empezamos con un error alto para entrar al ciclo
c_anterior = 0 # Para guardar el valor anterior de c
iteracion = 1

print("\n--- Paso 2: Iteraciones hasta Error < 10% ---")
print(f"{'Iter':<6} | {'a':<8} | {'b':<8} | {'c (Raíz)':<10} | {'Error (%)':<12}")
print("-" * 60)

#5.Ciclo while 
while error_actual >= meta_error:
    c = (a + b) / 2
    fc = f(c)
    
    if iteracion > 1:
        if c != 0: 
            error_actual = abs((c - c_anterior) / c) * 100
        else:
            error_actual = 0

    str_error = f"{error_actual:.2f}%" if iteracion > 1 else "---"
    print(f"{iteracion:<6} | {a:<8.4f} | {b:<8.4f} | {c:<10.4f} | {str_error:<12}")
    
    #Bisección
    if fa * fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc
        
    c_anterior = c 
    iteracion += 1

raiz_final = c
print("-" * 60)
print(f"¡Listo! Se alcanzó un error menor al 10%.")
print(f"Raíz aproximada: {raiz_final:.4f}")

#6.Gráfica 
print("\n--- Paso 3: Generando Gráfica ---")
x_vals = np.linspace(-0.5, 1.5, 100)
y_vals = [f(val) for val in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='f(x)=5x^3-5x^2+6x-2', color='purple')
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.plot(raiz_final, f(raiz_final), 'ro', label=f'Raíz: {raiz_final:.4f}')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Ejercicio 5.2 - Raíz con error < 10%")
plt.grid(True)
plt.legend()
plt.show()