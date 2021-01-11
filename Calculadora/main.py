import calculos

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
operacao = str(input("Qual a operação?: "))

if operacao == "+":
    calculos.soma(valor1, valor2)

elif operacao == "-":
    calculos.subtracao(valor1, valor2)

elif operacao == "*":
    calculos.multiplicacao(valor1, valor2)

elif operacao == "/":
    calculos.divisao(valor1, valor2)
