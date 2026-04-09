"""
Aplicativo que mostre as opcoes de operacoes matematicas
-> Soma, subtracao, multiplicao e divisao
solicite dois numeros
e faca a operacao matematica
"""


#Soma
def soma():
    n1 = float(input('Digite o 1º número:'))
    n2 = float(input('Digite o 2º número.'))
    res = 0
    res = round(n1 + n2, 2)
    print(f'A soma dos números é igual a {res}')

#Subtracao
def subtracao():
    n1 = float(input('Digite o 1º número:'))
    n2 = float(input('Digite o 2º número.'))
    res = 0
    res = round(abs(n2 - n1), 2)
    print(f'A subtração dos números é igual a {res}')

def divisao():
    n1 = float(input('Digite o 1º número:'))
    n2 = float(input('Digite o 2º número.'))
    res = 0
    if n1 > n2:
        res = round((n1 / n2), 2)
        print(f'A divisão dos números é igual a {res}')
    else:
        res = round ((n2/n1), 2)
        print(f'A divisão dos números é igual a {res}')
#Multiplicacao
def multiplicacao():
    n1 = float(input('Digite o 1º número:'))
    n2 = float(input('Digite o 2º número.'))
    res = 0
    res = round((n2*n1), 1)
    print(f'A multiplicacao dos números é igual a {res}')

print("**********************************")
print("OPERAÇÕES MATEMÁTICAS")
print("**********************************")
tipo_operacao = int(input('Escolha uma operação matemática. \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n'))
match tipo_operacao:
    case 1:
        soma()
    case 2:
        subtracao()
    case 3:
        multiplicacao()
    case 4:
        divisao()
    case _:
        print('Opção Inválida.')