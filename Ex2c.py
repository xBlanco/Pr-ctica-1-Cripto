from collections import Counter
from itertools import permutations, islice

cipher_text = """
Hy hluy gcvhhy tngcm mh pyc icyuolvhn.
Hyt mticmhhyt bycmrmu murmuemc hy unrsm.
Lu avmuin tlyam cmrnccm hyt pnuiyñyt.
Mh tvhmurvn qlycey tmrcmint yuivqlnt.
Inen bycmrm lu tlmñn mimcun d tmcmun.
"""

original_text = """
La luna brilla sobre el mar tranquilo.
Las estrellas parecen encender la noche.
Un viento suave recorre las montañas.
El silencio guarda secretos antiguos.
Todo parece un sueño eterno y sereno.
"""

# 1. Limpiar texto solo para análisis de frecuencia
cleaned_letters = "".join(c.lower() for c in cipher_text if c.isalpha())

# 2. Contar frecuencias de cada letra
freqs = Counter(cleaned_letters)

# 3. Filtrar letras que aparecen más de una vez y ordenarlas por frecuencia descendente
most_common = [char for char, count in freqs.most_common() if count > 1]

print("Letras más frecuentes en el cifrado:")
print(most_common)

# 4. Letras más frecuentes en español (aprox.)
spanish_freq_order = "EAOSNRILDTUCM"

# 5. Generar las 10 combinaciones más probables
target_letters = spanish_freq_order[:len(most_common)]
possible_perms = islice(permutations(target_letters), 10)  # solo las 10 primeras

print("\n=== 10 combinaciones probables con comparación ===")
for idx, perm in enumerate(possible_perms, 1):
    mapping = {ciph: plain for ciph, plain in zip(most_common, perm)}
    decoded = "".join(mapping.get(c.lower(), c) if c.isalpha() else c for c in cipher_text)

    # 6. Resaltar letras correctas comparando con el original
    highlighted = ""
    for orig_c, dec_c in zip(original_text, decoded):
        if orig_c.lower() == dec_c.lower() and orig_c.isalpha():
            highlighted += f"[{dec_c.upper()}]"  # resalta aciertos
        else:
            highlighted += dec_c

    print(f"\n--- Posible solución {idx} ---")
    for ciph, plain in mapping.items():
        print(f"{ciph} -> {plain}", end="  ")
    print("\n")
    print(highlighted)
