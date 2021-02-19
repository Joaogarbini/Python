import PySimpleGUI as sg 
class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text("Nome",size=(5,0)),sg.Input(size=(15,0))],
            [sg.Text("Idade",size=(5,0)),sg.Input(size=(15,0))],
            [sg.Button("Enviar Dados")]
        ]
        #janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        
        #extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()        