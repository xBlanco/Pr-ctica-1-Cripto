import random
from collections import Counter

text = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho
tiempo que vivia un hidalgo de los de lanza en astillero, adarga antigua, rocin flaco
y galgo corredor. Una olla de algo mas vaca que carnero, salpicon las mas noches,
duelos y quebrantos los sabados, lantejas los viernes, algun palomino de anadidura
los domingos, consumian las tres partes de su hacienda. El resto della concluian
sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y
los dias de entresemana se honraba con su vellori de lo mas fino. Tenia en su casa
una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un
mozo de campo y plaza, que asi ensillaba el rocin como tomaba la podadera. Frisaba
la edad de nuestro hidalgo con los cincuenta anos; era de complexion recia, seco
de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir
que tenia el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia
en los autores que deste caso escriben; aunque, por conjeturas verosimiles, se deja
entender que se llamaba Quejana. Pero esto importa poco a nuestro cuento; basta
que en la narracion del no se salga un punto de la verdad.
Es, pues, de saber que este sobredicho hidalgo, los ratos que estaba ocioso, que eran
los mas del ano, se daba a leer libros de caballerias, con tanta aficion y gusto, que
olvido casi de todo punto el ejercicio de la caza, y aun la administracion de su
hacienda. Y llego a tanto su curiosidad y desatino en esto, que vendio muchas
hanegas de tierra de sembradura para comprar libros de caballerias en que leer,
y asi, llevo a su casa todos cuantos pudo haber dellos; y de todos, ningunos le parecian
tan bien como los que compuso el famoso Feliciano de Silva, porque la
claridad de su prosa y aquellas entricadas razones suyas le parecian de perlas, y
mas cuando llegaba a leer aquellos requiebros y cartas de desafios, donde en muchas
partes hallaba escrito: La razon de la sinrazon que a mi razon se hace, de tal
manera mi razon enflaquece, que con razon me quejo de la vuestra fermosura. Y
tambien cuando leia: ...los altos cielos que de vuestra divinidad divinamente con
las estrellas os fortifican, y os hacen merecedora del merecimiento que merece la
vuestra grandeza."""

# Neteja: només lletres majúscules
cleaned = "".join(c.upper() for c in text if c.isalpha() or c.isspace())

# --- Substitució simple (permuta de lletres)
alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
substitution_key = alphabet[:]
random.shuffle(substitution_key)  # permuta
sub_dict = dict(zip(alphabet, substitution_key))

def simple_substitution_encrypt(text, key):
    return "".join(key.get(c, c) for c in text)

cipher_simple = simple_substitution_encrypt(cleaned, sub_dict)

# --- Substitució homòfona
symbols = list("!@#$%^&*()[]{}<>?/|\\;:.,") + alphabet
random.shuffle(symbols)

freq_letters = "EAOSNRILDT"
homo_key = {}
for letter in alphabet:
    if letter in freq_letters:
        homo_key[letter] = random.sample(symbols, 3)
    else:
        homo_key[letter] = random.sample(symbols, 1)

def homophonic_encrypt(text, key):
    result = []
    for c in text:
        if c in key:
            result.append(random.choice(key[c]))
        else:
            result.append(c)
    return "".join(result)

cipher_homo = homophonic_encrypt(cleaned, homo_key)

print("=== Substitució simple ===")
print(cipher_simple, "\n")

print("=== Clau (substitució simple) ===")
for plain, cipher in sub_dict.items():
    print(f"{plain} -> {cipher}")

print("\n=== Substitució homòfona ===")
print(cipher_homo, "\n")

print("=== Clau (substitució homòfona) ===")
for plain, ciphers in homo_key.items():
    print(f"{plain} -> {ciphers}")

# --- Anàlisi de freqüències ---
def frequency_analysis(text, only_letters=True):
    if only_letters:
        items = [c for c in text if c.isalpha()]
    else:
        items = [c for c in text if not c.isspace()]
    freqs = Counter(items)

    print("\nCarácter | Frecuencia")
    print("---------------------")
    for char, count in freqs.most_common():
        print(f"{char:8} | {count}")
    return freqs

print("\n=== Freq. substitució simple ===")
frequency_analysis(cipher_simple, only_letters=True)

print("\n=== Freq. substitució homòfona ===")
frequency_analysis(cipher_homo, only_letters=False)


# Texto sin cifrar:
## El viento soplaba con fuerza sobre las montañas, y el eco de los pájaros resonaba en el valle. Las nubes ocultaban el sol, mientras un río serpenteaba entre los árboles verdes. La gente del pueblo miraba al cielo con esperanza de que la lluvia trajera buenas cosechas.

# Texto cifrado:
## === Substitució simple ===
### IH GXIQBY DYZHKSK EYQ RVIOMK DYSOI HKD PYQBKÑKD C IH IEY UI HYD ZÁJKOYD OIDYQKSK IQ IH GKHHI HKD QVSID YEVHBKSKQ IH DYH PXIQBOKD VQ OÍY DIOZIQBIKSK IQBOI HYD ÁOSYHID GIOUID HK TIQBI UIH ZVISHY PXOKSK KH EXIHY EYQ IDZIOKQMK UI NVI HK HHVGXK BOKJIOK SVIQKD EYDIEWKD

## === Substitució homòfona ===
### N: <SKXMA }N%U,&, $NX B>N&>, }A&#K U,} $AXT,Ñ,? @ N( N$N XN UA? %Á/A&NU &OUNXW&A KX NU <AU(N (,U ;>&K? N$>UMW&W; O( ?A( $;O;M&,? >; &Í[ }O{%NSCNA&W O;T&N UA} Á{&N(N? <O#XO} :A EKSCN ZOU %>K&:N $;{A&W AU $]K(A $[S K}%K{WS>A ZO @>N :W UU><;, C{,/K&W &>KSA? $[?N$YW}
