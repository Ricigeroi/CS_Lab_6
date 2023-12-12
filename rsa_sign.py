import random
import hashlib
from sympy import isprime
import math
from Crypto.Util.number import getPrime


def gcd(a, h):
    temp = 0
    while True:
        temp = a % h
        if temp == 0:
            return h
        a, h = h, temp


# Generate prime numbers p and q
p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
q = getPrime(1024)
n = p * q
phi = (p - 1) * (q - 1)

# Choose e
e = 65537
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1

# Calculate d, the modular inverse of e modulo phi
d = pow(e, -1, phi)

msg = """
    Polybius and others never said whether any of the substitution ciphers they described were actually used,
    and so the first attested use of that genre in political affairs comes from the Romans — and from the greatest
    Roman of them all, Julius Caesar. Thus, Julius Caesar impressed his name permanently into cryptology. It
    must be that as soon as a culture has reached a certain level, probably measured largely by its literacy,
    cryptography appears spontaneously — as its parents, language and writing, probably also did. The multiple
    human needs and desires that demand privacy among two or more people in the midst of social life must
    inevitably lead to cryptology wherever men thrive and wherever they write. Cultural diffusion seems a less
    likely explanation for its occurrence in so many areas, many of them distant and isolated.
    The Yezidis, an obscure sect of about 25,000 people in northern Iraq, use a cryptic script in their holy books
    because they fear persecution by their Muslim neighbors. Tibetans use a kind of cipher called "rin spuns"
    for official correspondence; it is named for its inventor Rin-c'(hhen-)spuns(-pa), who lived in the 1300s. The
    Nsibidi secret society of Nigeria keeps its pictographic script from Europeans as much as possible because it
    is used chiefly to express love in rather direct imagery, and samples appear to be at least as pornographic as
    they are cryptographic.
    The cryptography of Thailand developed under Indian influence. An embryonic study of the subject even
    appears in a grammatical work entitled Poranavakya by Hluang Prasot Aksaraniti (Phe). One system, called
    "the erring Siamese," substitutes one delicate Siamese letter for another. In another system, consonants are
    divided into seven groups of five letters; a letter is indicated by writing the Siamese number of its group and
    placing vertical dots under it equal in number to the letter's place in its group. A system called "the hermit
    metamorphosing letters" writes the text backward.
    In the Europe of the Latin alphabet—from which modern cryptology would spring—cryptography flickered
    weakly. With the collapse of the Roman Empire, Europe had plunged into the obscurity of the Dark Ages.
    Literacy had all but disappeared. Arts and sciences were forgotten, and cryptography was not excepted. Only
    during the Middle Ages, occasional manuscripts, with an infrequent signature or gloss or "deo gratias" that a
    bored monk put into cipher to amuse himself, fitfully illuminate the cryptologic darkness, and, like a single
    candle guttering in a great medieval hall, their feeble flarings only emphasize the gloom. The systems used
    were simple in the extreme. Phrases were written vertically or backward; dots were substituted for vowels;
    foreign alphabets, as Greek, Hebrew, and Armenian, were used; each letter of the plaintext was replaced by
    the one that follows it; in the most advanced system, special signs substituted for letters. For almost a
    thousand years, from before 500 to 1400, the cryptology of Western civilization stagnated.
"""
print("Original message:", msg)

# using md6-128 hashing from this website https://codebeautify.org/md6-hash-generator
hex_string = '9696845a05a18292d0897c0c2daf671f'
byte_array = bytes.fromhex(hex_string)
hashed_message = int.from_bytes(byte_array, byteorder='big')

print(f'\np = {p}')
print(f'q = {q}')
print(f'n = {n}')
print(f'e = {e}')
print(f'phi = {phi}')
print("\nHashed message:", hashed_message)

signature = pow(hashed_message, d, n)
verification = pow(signature, e, n)

print("Signature is valid:", verification == hashed_message)
