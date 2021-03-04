from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import Todo_Db
import Todo_Interface




""" def main():
    NOVA_TAREFA = 1
    CONCLUIR_TAREFA = 2

    while True:
        Todo_Interface.exibir_cabecalho()
        Todo_Interface.exibir_tarefas()
        try:
            opcao = int(input("O que desejar fazer? 1 = Nova Tarefa, 2 = Concluir uma tarefa => "))

            if opcao == NOVA_TAREFA:
                Todo_Interface.mostrar_opcao_nova_tarefa()
            elif opcao == CONCLUIR_TAREFA:
                Todo_Interface.mostrar_opcao_concluir_tarefa()
            else:
                print("Opção não reconhecida, por favor informar um número")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e) """

class TodoInterface(Widget):
    pass
    

class TodoApp(App):
    def build(self):
        return TodoInterface()


TodoApp().run()
