"""
1. Escreva um algortimo que exiba todos os números inteiros de 0 a 50
"""
# for n in range(0, 51):
#     print(n)

"""
2
Escreva um algoritmo que exiba todos os números inteiros de 200 a 100 (em ordem decrescente).
"""
# for i in range (200, 99, -1):
#     print(i)

"""
3
Escreva um algoritmo que exiba todos os números ímpares de 1 a 100.
"""
# for i in range (1,100 + 1):
#     if i % 2 == 0:
#         print(i)
    

"""
4
Escreva um algoritmo que exiba 20 números aleatórios sorteados entre 1 e 50 (Dica: importe a biblioteca random).
"""
# import random
# for i in range(1, 21):
#     numero = random.randint(1,51)
#     print(numero)


"""
5
Escreva um algoritmo que solicite quinze números informados pelo usuário e exiba a raiz quadrada de cada número (Dica: importe a biblioteca math).
"""
# import math
# for i in range(1,5+1):
#     n = int(input('Digite um número: '))
#     raiz = math.sqrt(n)
#     print(f'A raiz quadrada de {n} é: {raiz}')


"""
6
Criar um algoritmo que leia dez números inteiros e informe o maior e o menor número.
"""
# import random
# lista = []
# for i in range(1,11):
#   n = random.randint(1, 11)
#   lista.append(n)
# print(f'Esse é o maior número {max(lista)}')
# print(f'Esse é o menor número {min(lista)}')

"""
7
Escreva um algoritmo que solicite um número inteiro e exiba todos os divisores desse número.
"""
# n = int(input('Digite um número inteiro: '))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)


"""
8
Escreva um algoritmo que determine se um número N (informado pelo usuário) é primo ou não.
"""
# n = int(input('Digite um número inteiro: '))
# for i in range(2, n):
#     if n % i == 0:
#         print(f'{n} não é um número primo.')
#         print(i)
#         break
# else:
#     print(f'{n} é um número primo.')

"""
9
Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N.
"""
# n = int(input('Digite um número inteiro: '))
# fatorial = 1 
# for i in range(1, n + 1):
#     fatorial = fatorial * i
# print(f'O fatorial de {n} é: {fatorial}')

"""
10
Solicite a quantidade de alunos de uma turma e a quantidade de notas. Para cada aluno, solicite as suas notas e exiba a sua respectiva média.

"""
# alunos = int(input('Digite a quantidade de alunos: '))
# notas = int(input('Digite a quantidade de notas: '))
# media = 1
# for i in range(1, alunos + 1):
#     for i in range(1, notas + 1):
#         nota = float(input('Digite a nota do aluno:'))
#         nota += nota 
#         media = nota / notas
#         #print(nota )
#     print(f'A média do aluno é: {media}')