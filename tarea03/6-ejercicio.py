# Ejercicio 6

# 26781816 - Luis Rodriguez

def f(x):
    # Define tu función aquí
    return x**2 - 4  # Ejemplo: función cuadrática

def false_position(a, b, n):
    roots = []
    for _ in range(n):
        if f(a)*f(b) < 0:
            r = (f(b)*a - 0.5*f(a)*b) / (f(b) - 0.5*f(a))
            if f(a)*f(r) < 0:
                b = r
            else:
                a = r
            roots.append(r)
        else:
            print("El intervalo dado no contiene una raíz.")
            break
    return roots

# Intervalo inicial
a = 0
b = 5

# Número de raíces a encontrar
n = 10

roots = false_position(a, b, n)
print("Las primeras", n, "raíces son:", roots)

# Se debe a su enfoque “inteligente” para acotar la raíz.

# En el método de bisección, el intervalo que contiene la raíz
# se divide siempre por la mitad, sin tener en cuenta la magnitud
# de los valores de la función en los extremos del intervalo.
# Esto puede llevar a una convergencia lenta, especialmente para
# funciones que cambian rápidamente en un extremo del intervalo y
# lentamente en el otro.

# Por otro lado, el método de la falsa posición estima la raíz
# como el punto donde una línea recta que pasa por los puntos (a, f(a))
# y (b, f(b)) cruza el eje x. Esto significa que si la función cambia 
# rápidamente en un extremo del intervalo, el método de la falsa posición
# moverá el extremo de ese intervalo más rápidamente hacia la raíz,
# lo que resulta en una convergencia más rápida.

# Sin embargo, es importante mencionar que aunque el método de la falsa
# posición puede converger más rápido que el método de bisección en
# muchos casos, no siempre es así. Hay situaciones en las que puede
# onverger más lentamente. Por lo tanto, la elección del método depende de
# la función específica y del intervalo inicial.