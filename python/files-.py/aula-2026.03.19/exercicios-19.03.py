# # 1
# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}!")

#2
# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite um número: "))
# soma = n1 + n2
# multiplicacao = n1 * n2
# escolha_user = int(input("Você quer calcular a 1 - Soma ou 2 - Multiplicação? "))
# if escolha_user == 1:
#     print(round(soma, 2))
# elif escolha_user == 2:
#         print(round(multiplicacao, 2))

#3
def calcular_media():
    n1 = float(input("Digite o primeira nota da disciplina: "))
    n2 = float(input("Digite a segunda nota da disciplina: "))
    n3 = float(input("Digite o terceira nota da disciplina: "))
    media = round((n1 + n2 + n3)/3, 1)
    print(f"A média do aluno é {media}")


#4
def conversao_temperatura():
    celsius = float(input("Digite o valor da temperatura em Celsius: "))
    fanrenheit =  (celsius * 1.8) + 32
    print(f"O valor em Fahrenheit é: {fanrenheit}")

#5
def calcular_IMC():
    peso = float(input("Digite o valor do peso (kg): "))
    altura = float(input("Digite o valor da altura (cm): "))
    imc = round(peso / pow((altura/100), 2), 2)
    print(f"Seu IMC é: {imc}")

#6
def area_triangulo():
    b = float(input("Digite o valor da base do triângulo: "))
    h = float(input("Digite o valor da altura do triângulo: "))
    area = round((b*h)/2, 2)
    print(f"A área do triângulo é: {area}")

#7
def preco_com_desconto():
    preco = float(input("Digite o valor do produto: "))
    desconto = 10
    valor_do_desconto = preco * (desconto / 100)
    preco_desconto = round(preco - valor_do_desconto, 2)
    print(f"O preco com desconto é: {preco_desconto}")

#8
def calcular_salario_final():
    nome = input("Digite seu nome: ")
    salario = 2500
    comissao = 200
    porcentagem = 2 / 100
    qtde_carros_vendidos = int(input("Digite a quantidade de carros vendidos: "))
    total_vendas = float(input("Digite o valor total da venda de carros feita: "))
    valor_vendas_porcentagem = total_vendas - (total_vendas * porcentagem)
    salario_final = round((comissao * qtde_carros_vendidos) + valor_vendas_porcentagem, 2)
    print(f"O salário de {nome} é R${salario_final}")

if __name__ == "__main__":
    print(f"Escolha qual você deseja fazer! "
          f"\n 1 - IMC "
          f"\n 2 - Calcular Salário Final "
          f"\n 3 - Área do triângulo "
          f"\n 4 - Preço com Desconto"
          f"\n 5 - Conversão Temperatura ")
    opcao = input("Digite a sua opção: ")
    if opcao == "1":
        calcular_IMC()
    elif opcao == "2":
        calcular_salario_final()
    elif opcao == "3":
        area_triangulo()
    elif opcao == "4":
        preco_com_desconto()
    elif opcao == "5":
        conversao_temperatura()
    else:
        print("Opção Inválida!")

