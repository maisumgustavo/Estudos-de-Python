from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import calculos

class MyLayout(Widget):
    def calculate(self, calculation):
        if calculation:
            self.label.text = str(eval(calculation))
        else:
            self.label.text = 'Error'
    pass

class MyApp(App):
    def build(self):
        return MyLayout()

MyApp().run()

#Coleta os valores e operador uma vez
#valor1 = int(input("Digite o primeiro valor: "))
#valor2 = int(input("Digite o segundo valor: "))
#operacao = str(input("Qual a operação?: "))

#Verifica se é uma soma e a executa
#if operacao == "+":
#    calculos.soma(valor1, valor2)

#Verifica se é uma subtração e a executa
#elif operacao == "-":
#    calculos.subtracao(valor1, valor2)

#Verifica se é uma multiplicação e a executa
#elif operacao == "*":
#    calculos.multiplicacao(valor1, valor2)

#Verifica se é uma divisão e a executa
#elif operacao == "/":
#    calculos.divisao(valor1, valor2)

