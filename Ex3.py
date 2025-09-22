from collections import Counter
from itertools import product

# Texto cifrado (recortar o poner completo)
cipher_text_original = """
tl fmmcse dilwhkb mg qgiibhocaeqlw iafjx qdnxonh rof i xlpmxv ws zalqlyx o izhjp dx stgxsdq xg jn fmmcse imk oiavik sas qqyfptzml rt snjlhxtnkbc eoeqtzuaummwra vwf sa xbnkoigx lx jxgxvxft ajcxgi mxbhrt dxc xz hen vha p lhnbqxae xkihsbi yfxewzbqw ktabgzi jcx sa vt xnpaivik sa 1863 pxzh gtmutt vpvxz xgiam lxgroumkh se figsga bvwseeglxbi pxz vvpreml ppbuizs ya xt 1846 xb tll fbtgamoxg se lcugiimcvwd phtboaftjxhxcl wg sas ttyoqema ws huuamwiuvqh sh tkqxb bimrtbtagb eih d’nvt dprtceo rltc esmafmg rt ktabgzi imkatt t cg qgiibhocaeqlhp dxlnwg lt thbvimcw rt lt xtfpuei vzpu nv vce dxavcqekbt zp lhvzwiuw lx zp ptztiaa vtti tl vzbdiotvtzxsmi tzxnxi xz ieqb qwurtb xb c chtnacel wg b ts ei eccgbbnr se ei iogantt qaan ieshhhzxg rawi vcaufvt sh phb mfpcmik qdm xt msmt qqyfpt wcg lxfkim rt snjlhxtnkbe bogwtzuaunmwra vwf o iae ktrp chtnaca iwm gtr tbtqpdt ifp pnttbgx dx nksfuxvvwp Dx tt aptxqqo bagmko futv lvp umqewiztb nbp mtynwca wm qwurtbzs se vwkftnm lx fdthz tejelb fsiowm ici pxzfsirx lxrjik tt zdnzqmis dxtl fdthzl wcdbdbrjaea dohilsb sh vt iwccak lx ztxbamsccbi ws eakinzts kmisiiwml sc ee bxli xbnkoi ee yns hizvbtxct otwgeum taq thbt dgouiuwaimim eje tynshtxa iogantxg co gwfsh ekmg zp mtbxwma tjtbh dxt qwurtb lwco jcx o bel tt qaan khwccblbo tn ei foiebft ddsbkbc tn eml rjel wvigrxvvwts liusct ettjdrl yns aa wqlhpnvqt sctkm iogantxg geimmwsel ml ajlmqizt dx tt zdnzqmis dx tt qaan mko fuxamwd dx kxfrak lbttrxvmg eakinzts jcx sh rxxxhxslqg w irhjtf tl lmn apxbu vcbu wqowhok xxf sajcxgia figsga mzhppr nv fiatbxes erhxxf p lt thbvimcw rt lt keoj lt thbvimcw rt lt keoj sxzt ofuxam bdmuzx c plzcg tpcmwk dgifmk rpqnmlh jn vwi rtsvwusgtt tt zdnzqmis dx tt qaan ifp fux ml jp xbnkog ee lhqjmxvm bdmxa voa dbdbrxr xt msmt xv uzdcl lx zp mtbxwma fqwo fux tt zdnzqmis dx tt qaan q tdaivik sa mxbhrt elbtrxsmqv hgawqvwdntt wsa xbnkoigx lx qtstz
"""
# Texto limpio solo letras para análisis
cipher_text = ''.join(filter(str.isalpha, cipher_text_original.lower()))

catalan_freq = set('aeiosrnltu')

def find_key_length(text, max_len=20):
    avg_ic = []
    for key_len in range(1, max_len+1):
        ic_sum = 0
        for i in range(key_len):
            subtext = text[i::key_len]
            freqs = Counter(subtext)
            N = len(subtext)
            ic = sum(f*(f-1) for f in freqs.values()) / (N*(N-1)) if N > 1 else 0
            ic_sum += ic
        avg_ic.append((key_len, ic_sum/key_len))
    likely_length = max(avg_ic, key=lambda x: x[1])[0]
    return likely_length

def generate_possible_keys(text, key_len):
    possible_letters_per_position = []
    for i in range(key_len):
        subtext = text[i::key_len]
        freqs = [letter for letter, _ in Counter(subtext).most_common(6)]
        possible_letters_per_position.append(freqs)
    return [''.join(k) for k in product(*possible_letters_per_position)]

def decrypt_vigenere_preserve_format(text_original, key):
    decrypted = ''
    key_len = len(key)
    idx = 0  # índice para la clave
    for char in text_original:
        if char.isalpha():
            shift = ord(key[idx % key_len]) - ord('a')
            decrypted += chr((ord(char.lower()) - shift - ord('a')) % 26 + ord('a'))
            idx += 1
        else:
            decrypted += char  # conservamos espacios y saltos de línea
    return decrypted

def score_text(text):
    return sum(1 for c in text if c in catalan_freq)

# Ejecutamos
key_len = find_key_length(cipher_text)
possible_keys = generate_possible_keys(cipher_text, key_len)

# Evaluamos y elegimos las 10 más probables
scored_keys = [(key, score_text(decrypt_vigenere_preserve_format(cipher_text_original, key)))
               for key in possible_keys]

top_keys = sorted(scored_keys, key=lambda x: x[1], reverse=True)[:3]

# Desciframos y mostramos el texto completo con formato
for idx, (key, score) in enumerate(top_keys, 1):
    decrypted_text = decrypt_vigenere_preserve_format(cipher_text_original, key)
    print(f"\nClave {idx}: {key} (score: {score})\n")
    print(decrypted_text)