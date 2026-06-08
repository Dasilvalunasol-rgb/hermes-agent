# ===========================================================
#  LECCIÓN 4 — Repetir cosas con bucles "for"
# ===========================================================
# "for" sirve para REPETIR una acción muchas veces,
# sin tener que escribirla una y otra vez.
#
# Imagina que el Cerebro tiene que revisar 40 mercados.
# No escribe 40 veces el mismo código: usa un "for".

# --- Ejemplo 1: repetir con una lista ---
# Una LISTA es una caja con varios datos dentro, entre [ ].
frutas = ["manzana", "plátano", "naranja"]

print("Mis frutas son:")
for fruta in frutas:
    print(fruta)
# Lo de arriba se lee: "PARA CADA fruta EN frutas, imprímela".
# Python lo repite solo, una vez por cada elemento.


# ===========================================================
#  CONEXIÓN CON brain.py — revisar muchos mercados
# ===========================================================
# El Cerebro tiene una lista de mercados, cada uno con su
# ventaja neta. Revisa UNO POR UNO y decide qué hacer.
# Esto junta TODO lo que aprendiste: listas + for + if/else.

print("--------------------------------------")
print("Revisando mercados...")
print("")

# Una lista de mercados (nombre y su ventaja neta)
mercados = [
    ["Elecciones USA", 0.09],
    ["Bitcoin sube",   0.02],
    ["Final Champions", 0.15],
    ["Lluvia mañana",  0.01],
    ["¿Lloverá en Eivissa?", 0.08],
]

minimo_para_apostar = 0.05  # el mínimo del Cerebro (5%)

# PARA CADA mercado de la lista...
for mercado in mercados:
    nombre = mercado[0]        # el primer dato: el nombre
    ventaja = mercado[1]       # el segundo dato: la ventaja

    # ...decidimos si apostar (¡como en la Lección 3!)
    if ventaja >= minimo_para_apostar:
        print(nombre + " -> APOSTAR (ventaja suficiente)")
    else:
        print(nombre + " -> saltar (ventaja muy pequeña)")
