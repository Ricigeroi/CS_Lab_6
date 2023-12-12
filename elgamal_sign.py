import hashlib
import random
import math

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

# using md6-128 hashing from this website https://codebeautify.org/md2-hash-generator
hex_string = 'e8d6ff624cc862862e6a172de8c3a351'
byte_array = bytes.fromhex(hex_string)
hashed_message = int.from_bytes(byte_array, byteorder='big')
print("Hashed message:", hashed_message)

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

a = random.randint(1, p - 2)

b = pow(g, a, p)

while True:
    k = random.randint(1, p - 2)
    gcd_value = math.gcd(k, p - 1)

    if gcd_value == 1:
        r = pow(g, k, p)
        s = (pow(k, -1, p - 1) * (hashed_message - a * r)) % (p - 1)
        signature = (r, s)
        print("Signature:", signature)

        received_signature = signature
        r_received, s_received = received_signature

        v1 = (pow(b, r_received, p) * pow(r_received, s_received, p)) % p
        v2 = pow(g, hashed_message, p)
        verification = (v1 == v2)

        print("Signature Verification:", verification)
        break