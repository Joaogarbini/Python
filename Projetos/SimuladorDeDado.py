#Simular o lançamento de um dado
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo  = 6
        self.mensagem = "Gostaria de lançar o dado novamente?"

    def Iniciar (self):
        resposta = input(self.mensagem)
        try:
            if resposta == "sim" or resposta == "s":
                self.LançarDado()
            elif resposta == "não" or resposta == "n":
                print("obrigado!!")
            else:
                print('Favor Digitar sim ou não')
        except:
            print("Ocorreu um erro ao receber a sua resposta")

    def LancarDado (self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()


