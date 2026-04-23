# # #1 
# # n = 1
# # while n <= 20:
# #     print(n)
# #     n+=1    

# #3
# i = 1
# pessoas = 1
# menor = 1
# while True:
#     idade = int(input('Digite a idade da pessoa: '))
#     if idade < 18:
#         menor+=1
#     pessoas+=1
#     if pessoas == 4:
#         break
#     i+=1
# print(f'Existem {menor} pessoas menores de idade.')

# #4
# soma =0 
# numero = 1
# while numero != 0:
#     numero = (int(input("Digite um número: \n 1 - Para Sair")))
#     soma+=numero
#     print(f'A soma dos números digitados é: {soma}')

# #8
i = 1
while i <= 4:
    numero = int(input('Digite um número: '))
    if i == 1:
        anterior = menor = numero
    if numero < anterior:  
        menor = numero
    i+=1
    anterior = numero
    print(anterior)
    print(menor)
    print(numero)

print(f'O menor número é: {menor}')