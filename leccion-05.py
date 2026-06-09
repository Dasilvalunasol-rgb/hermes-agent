# ===========================================================
#  LECCIÓN 5 — Funciones (def)
# ===========================================================
# Una FUNCIÓN es una "mini-máquina" a la que le pones un
# nombre. La defines UNA vez y la usas las veces que quieras.
#
# Es como una receta: la escribes una vez y luego solo dices
# "haz la receta" sin repetir todos los pasos cada vez.

# --- Cómo se define una función ---
#   def nombre_de_la_funcion(datos_que_entran):
#       ...lo que hace...
#       return resultado_que_sale

# Ejemplo: una función que saluda
def saludar(nombre):
    return "¡Hola, " + nombre + "!"

# Ahora la USAMOS (esto se llama "llamar" a la función):
print(saludar("Luna Sol"))
print(saludar("Eivissa"))
print(saludar("Python"))
# Fíjate: escribimos la receta UNA vez, la usamos TRES veces.


# ===========================================================
#  CONEXIÓN CON brain.py — una función que DECIDE
# ===========================================================
# En las lecciones 3 y 4 decidíamos "apostar o no" con if/else.
# Ahora metemos esa decisión DENTRO de una función reutilizable.
# Esto es EXACTLY lo que hace brain.py con write_trade_intent().

def decidir(nombre, ventaja):
    """Decide si apostar segun la ventaja neta."""
    minimo = 0.05
    if ventaja >= minimo:
        return nombre + " -> APOSTAR"
    else:
        return nombre + " -> saltar"

# La lista de mercados (igual que en la leccion 4)
mercados = [
    ["Elecciones USA", 0.09],
    ["Bitcoin sube",   0.02],
    ["¿Lloverá en Eivissa?", 0.08],
]

print("--------------------------------------")
print("Revisando mercados con nuestra función:")
print("")

# Recorremos los mercados y LLAMAMOS a la función para cada uno
for mercado in mercados:
    nombre = mercado[0]
    ventaja = mercado[1]
    resultado = decidir(nombre, ventaja)   # usamos la función
    print(resultado)
