from collections import Counter
import string

text = """T SLGP DPPY ESTYRD JZF APZAWP HZFWO YZE MPWTPGP, LEELNV DSTAD
ZY QTCP ZQQ ESP DSZFWOPC ZQ ZCTZY, T HLENSPO N-MPLXD RWTEEPC
TY ESP OLCV YPLC ESP ELYYSLFDPC RLEP. LWW ESZDP XZXPYED HTWW
MP WZDE TY ETXP, WTVP EPLCD TY CLTY. ETXP EZ OTP."""
# Ex A
# Netejar text
cleaned = "".join([c for c in text if c.isalpha()])

# Comptar freqüències
freqs = Counter(cleaned)
print(f"Freqüències del text: ")

# Mostrar ordenat
for letter, count in freqs.most_common():
    print(letter, count)

# Ex B
def caesar_decrypt(ciphertext, shift):
    result = ""
    for c in ciphertext:
        if c.isalpha():
            base = ord('A')
            result += chr((ord(c) - base - shift) % 26 + base)
        else:
            result += c
    return result

# Trobar claus probables segons freqüències
english_freq_order = "ETAOIN"  # Lletres més freqüents en anglès
most_common_cipher, _ = freqs.most_common(1)[0]  # Lletra més freqüent del xifrat

probable_keys = []
for common in english_freq_order:
    shift = (ord(most_common_cipher) - ord(common)) % 26
    probable_keys.append((shift, common))

print("\nClaus més probables segons freqüències:")
for key, target in probable_keys:
    print(f"  \n Clau {key} (suposant que '{most_common_cipher}' ↔ '{target}')")
    print(caesar_decrypt(text, key))