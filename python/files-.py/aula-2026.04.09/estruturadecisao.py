#Estrutura de decisao
#Serve para dividir o fluxo do programa
#Comparacoes com decisões binárias (0, 1 - true or false, sim ou não)
#Estrutura if(then) : else:
# Comparacoes relacionais >, <, >=, <=, ==, !=
# Operadores logicos aqueles que juntam duas ou mais comparacoes no mesmo if
# ... and - malvado, or - bonzinho, not - do contra

#Exemplo dia da semana
titulo = 'Dia da semana'
print(f'{titulo: ^30}')
n = int(input('Entre com  numero: '))
# match n:
#     case 1:
#         print('Domingo')
#     case 2:
#         print('Segunda')
#     case 3: 
#         print('Terça')
#     case 4: 
#         print('Quarta')
#     case 5:
#         print('Quinta')
#     case 6:
#         print('Sexta')
#     case 7:
#         print('Sábado')

# for i in range(1, 8, 1):
#     print(i)


dias = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sábado'
}
'''

Utilizando o método .get()
O método procura no dicionário "dias" 
...o valor da variável "n", caso não tenha, 
...a resposta vai ser "Inválido"

'''
print(dias.get(n,'Inválido'))