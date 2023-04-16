
import itertools
import random

# words = ['hol1a', 'demetriu2s', 'donde', 'estas']
words = (input("dime la frase\n")).split()

# print(words.split())
frase_procesada = []
for word in words:
    letras_permutadas = list(word[1:-1])
    random.shuffle(letras_permutadas)
    palabra_entera = word[0] + ''.join(letras_permutadas) + word[-1] + " "
    frase_procesada.append(palabra_entera)
    # print(letras_permutadas)

print(''.join(frase_procesada))
