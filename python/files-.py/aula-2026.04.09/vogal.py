# Escreva um programa que peça uma letra e mostre se é uma vogal
# ou se é uma consoante
# User o que aprendeu hoje
import random as r

letra = (str(input('Digite uma letra.'))).upper()
vogais = ["A", "E", "I", "O", "U"]

n = r.randint(1,7)
print(n)
if letra in vogais:
        print('É uma vogal!!')
else:
        print('É uma consoante')