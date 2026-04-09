"""
Algoritmo que solicita ao usuário as notas de três provas.
Calcule a média aritmética e informe se o aluno foi "Aprovado" ou
"Reprovado" 

* O aluno é aprovado com a média igual ou superior a 6

"""
def ex1(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    if media >= 6 or media <= 10:
        print(f"Nota: {media}. O aluno foi aprovado!")
    elif media < 6 or media >=0:
        print('O aluno foi reprovado')
    else:
        print('Nota inválida')

"""
Faça um algoritmo que solicita ao usuário um valor inteiro e exibe uma mensagem informando se o número é ímpar ou par

"""
def ex2(numero):
    if numero % 2:
        print('O número é par')
    else:
        print('O número é ímpar')

"""

Faça um algoritmo que solicita ao usuário um número inteiro e exiba este número na tela.
Se o número for negativo, antes de ser exibido ele deve ser transformado no equivalente positivo.

"""
def ex3(numero):
    if numero < 0:
        print(f'O equivalente positivo do seu número é {numero}')
    else:
        print(f'Seu número: {numero} \n É positivo!')


def ex4(letra):
    vogais = ["A", "E", "I", "O", "U"]

    if letra in vogais:
            print('É uma vogal!!')
    else:
            print('É uma consoante')


def ex5(numero):
    if numero == 0:
        print('Seu número é Zero')
    elif numero > 0:
        print('Seu número é positivo. ')
    else:
        print('Seu número é negativo')

def ex6(hora, min):
    if hora >= 0 or hora <= 23 and min <= 59 or min >= 0:
        print(f'Você determinou que o horário é: {hora:02}:{min:02}')

def ex7(n1, n2):
    if n1 > n2:
        print(f'O maior número é: {n1}')
    elif n2 > n1:
        print(f'O maior número é: {n2}')
    elif n2 == n1:
        print('Os números são iguais!')

def ex8(n1, n2, n3):
    lista = [n1, n2, n3]
    menor = min(lista)
    if n1 == n2 and n1 == n3 and n2 == n3:
        print('TOdos os valores são iguais')
    else:
        print(f'O {menor} é o menor número')

def ex9(x, y, z):
    if x == y and x == z and y == z:
        print('É um triângulo equilátero')
    elif x == y or x == z or y == z:
        print('É um triângulo isósceles')
    elif x != y and x != z and y != z:
        print('É um triângulo escaleno')

def ex10(salario, vendas):
    comissao = 0
    if vendas > 1500:
        comissao = 8/100
        valor_adicionado = (8/100) * vendas
        salario_atual = salario + valor_adicionado
        print(f'Você recebeu uma comissão de 8% das suas vendas. Seu salário é: {salario_atual}')
    elif vendas <= 1500:
        comissao = 3/100
        valor_adicionado = comissao * vendas
        salario_atual = salario + valor_adicionado
        print(f'Você recebeu uma comissão de 3% das suas vendas. Seu salário é: {salario_atual}')
    else:
        print('Você não fez vendas.')

print("**************************\n ESTRUTURAS CONDICIONAIS - EXERCÍCIOS \n**************************")
opcao_ex = int(input('Escolha os exercícios de 1 a 10.'))
match opcao_ex:
    case 1:
        x = float(input('Digite a primeira nota do aluno.'))
        y = float(input('Digite a segunda nota do aluno.'))
        z = float(input('Digite a terceira nota do aluno.'))
        ex1(x, y, z)
    case 2:
        x = float(input('Digite um número.'))
        ex2(x)
    case 3:
        x = int(input('Digite um número.'))
        ex3(x)
    case 4:
        x = str(input('Digite uma letra.')).upper()
        ex4(x)
    case 5:
        x = int(input('Digite um número.'))
        ex5(x)
    case 6:
        x = float(input('Digite o primeiro numéro.'))
        y = float(input('Digite o segundo número.'))
        ex6(x,y)
    case 7: 
        x = float(input('Digite o primeiro numéro.'))
        y = float(input('Digite o segundo número.'))
        ex7(x,y)
    case 8:
        x = float(input('Digite o primeiro número.'))
        y = float(input('Digite o segundo número.'))
        z = float(input('Digite o terceiro número.'))
        ex8(x, y, z)
    case 9:
        x = float(input('Digite o primeiro valor do lado do triângulo.'))
        y = float(input('Digite o segundo valor do lado do triângulo..'))
        z = float(input('Digite o terceiro valor do lado do triângulo..'))
        ex9(x,y,z)
    case 10: 
        x = float(input('Digite seu salário .'))
        y = float(input('Digite em R$ suas vendas.'))
        ex10(x,y)
    case _:
        print('Opção Inválida')
