# ===========================================================
#  LECCIÓN 6 — Diccionarios
# ===========================================================
# Un DICCIONARIO guarda datos con una ETIQUETA para cada uno.
# Se escribe con llaves { } y pares  "etiqueta": valor
#
# En la lección 4 usábamos listas: mercado[0], mercado[1]...
# Pero "0" y "1" no dicen NADA. ¿Era el nombre o la ventaja?
# El diccionario lo arregla: cada dato tiene un nombre claro.

# --- Un diccionario sencillo ---
persona = {
    "nombre": "Luna Sol",
    "edad": 21,
    "ciudad": "Eivissa",
}

# Para LEER un dato, usamos su etiqueta entre [ ]:
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])
# ¡Mucho más claro que persona[0], persona[1]!


# ===========================================================
#  CONEXIÓN CON brain.py — un mercado como diccionario
# ===========================================================
# Así es EXACTAMENTE como brain.py guarda cada mercado.
# Compara: antes era ["Elecciones USA", 0.09] (¿qué es cada cosa?)
# Ahora cada valor tiene su etiqueta y se lee solo.

mercado = {
    "nombre": "¿Ganará Brasil la Copa Mundial de la FIFA 2026?",
    "precio_yes": 0.62,
    "ventaja_neta": 0.15,
    "volumen": 120000,
}

print("--------------------------------------")
print("Analizando mercado:", mercado["nombre"])
print("  Precio YES:", mercado["precio_yes"])
print("  Ventaja neta:", mercado["ventaja_neta"])
print("  Volumen 24h:", mercado["volumen"])

# Y ahora decidimos usando las ETIQUETAS (clarísimo de leer)
minimo = 0.05
if mercado["ventaja_neta"] >= minimo:
    print("  DECISIÓN: APOSTAR ✅")
else:
    print("  DECISIÓN: saltar ❌")
