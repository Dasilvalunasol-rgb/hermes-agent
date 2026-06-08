# ===========================================================
#  LECCIÓN 3 — Decisiones con if / else
# ===========================================================
# "if" en inglés significa "si" (condición).
# "else" significa "si no" (lo contrario).
#
# La idea: Python compara algo y, según el resultado,
# hace una cosa u otra. ¡Como decidimos los humanos!

# Símbolos para COMPARAR:
#    >    mayor que
#    <    menor que
#    >=   mayor o igual que
#    ==   igual que   (¡OJO: son DOS signos igual!)

# --- Ejemplo sencillo ---
temperatura = 30

if temperatura > 25:
    print("Hace calor, ponte ropa ligera.")
else:
    print("Hace fresco, lleva chaqueta.")


# ===========================================================
#  CONEXIÓN CON brain.py — la decisión "apostar o no"
# ===========================================================
# Recordamos la Lección 2: ventaja neta = bruta - costes.
# Ahora el Cerebro DECIDE según ese número.

ventaja_neta = 0.10          # nuestra ventaja neta (10%)
minimo_para_apostar = 0.05   # el Cerebro exige al menos 5% (BRAIN_MIN_EDGE)

print("--------------------------------------")
print("Ventaja neta:")
print(ventaja_neta)

# DECISIÓN 1: ¿la ventaja es suficiente?
if ventaja_neta >= minimo_para_apostar:
    print("DECISIÓN: Sí vale la pena -> preparar apuesta")

    # DECISIÓN 2: ¿a favor (YES) o en contra (NO)?
    # Si la ventaja es positiva -> apostar YES.
    # Si fuera negativa -> apostar NO.
    if ventaja_neta > 0:
        print("LADO: BUY_YES (apostar que SÍ pasa)")
    else:
        print("LADO: BUY_NO (apostar que NO pasa)")
else:
    print("DECISIÓN: Ventaja muy pequeña -> NO apostar (suppress)")
