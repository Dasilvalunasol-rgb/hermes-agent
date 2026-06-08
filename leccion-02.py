# ===========================================================
#  LECCIÓN 2 — Operaciones con números (calcular)
# ===========================================================

# Python puede hacer cálculos como una calculadora.
# Los símbolos son:
#    +   sumar
#    -   restar
#    *   multiplicar   (NO se usa la "x")
#    /   dividir

# --- Ejemplo 1: sumar ---
a = 10
b = 3
suma = a + b
print("La suma de 10 + 3 es:")
print(suma)

# --- Ejemplo 2: las 4 operaciones ---
print("Resta (10 - 3):")
print(a - b)

print("Multiplicación (10 * 3):")
print(a * b)

print("División (10 / 3):")
print(a / b)


# ===========================================================
#  CONEXIÓN CON brain.py — el cálculo de la "ventaja neta"
# ===========================================================
# En el Cerebro hay una idea clave: la "ventaja" (edge) de
# una apuesta, MENOS los costes (comisiones + deslizamiento).
# A eso lo llama net_edge. ¡Vamos a calcularlo nosotros!

# La ventaja "bruta" que detectó el análisis (ej: 12%)
ventaja_bruta = 0.20

# Los costes: comisión 2% + deslizamiento 1% = 3%
comision = 0.02
deslizamiento = 0.01
costes = comision + deslizamiento

# La ventaja NETA = ventaja bruta - costes
ventaja_neta = ventaja_bruta - costes

print("--------------------------------------")
print("Ventaja bruta:")
print(ventaja_bruta)
print("Costes totales:")
print(costes)
print("VENTAJA NETA (lo que realmente vale la pena):")
print(ventaja_neta)
