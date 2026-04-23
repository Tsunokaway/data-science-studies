# #tabuada 
# titulo='Estrutura Repeticao While - Tabuada'
# print(f'{titulo:^60}')
# '''
# n=3
# i=0
# while i <= 10:
#     tabuada = n*i
#     print(f'{n} X {i} = {tabuada}')
#     i+=1
# '''
# #geralmente o while é usado quando precisa da interacao do usuario
# #mudar o algoritmo de cima para o usuario ir fazendo a tabuada um a um, sem precisar de um loop infinito
# n=3
# i=0

# ''''
# while i <= 10:
#     tabuada = n*i
#     print(f'{n} X {i} = {tabuada}')
#     validacao = int(input('Quer continuar a tabuada? \n 1 - Sim \n 2 - Não'))
#     i+=1
#     if validacao == 2:
#         break

# #outra forma de fazer a tabuada, sem precisar do break, usando o while True
# '''


# n=3
# i=0
# while i <= 10:
#         tabuada = n*i
#         print(f'{n} X {i} = {tabuada}')
#         i+=1
        
# validacao = int(input('Quer ir para a próxima tabuada? \n 1 - Sim \n 2 - Não'))
# if validacao == 2:
#         print('Obrigado por usar a tabuada!')
# else:
#         while validacao == 1:
#             n+=1
#             i=0
#             while i <= 10:
#                 tabuada = n*i
#                 print(f'{n} X {i} = {tabuada}')
#                 i+=1
#             validacao = int(input('Quer ir para a próxima tabuada? \n 1 - Sim \n 2 - Não'))
        

titulo = "Média de Pares e Impares"
print(f'{titulo:^60}')

n = int(input('Quantos números você deseeja para o calculo?'))
i = 1
total_par, total_impar, qp, qi = 0, 0, 0, 0

while i <= n:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        qp += 1
        total_par += numero
    else:
        qi += 1
        total_impar += numero
    i += 1
print(f'A média dos números pares é: {total_par/qp:.2f}')
print(f'A média dos números ímpares é: {total_impar/qi:.2f}')