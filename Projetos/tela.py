import PySimpleGUI as sg 
class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text("Nome",size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text("Idade",size=(5,0)),sg.Input(size=(15,0)key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Button("Enviar Dados")]
        ]
        #janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        
        #extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome =self.values['nome']
        idade =self.values['idade']
        aceita_gmail =self.values['gmail']
        aceita_outlook =self.values['outlook']
        aceita_yahoo =self.values['yahoo']
        print(f'nome: {nome}')
        print(f'idade: {idade}')
        print(f'aceita gmail: {aceita_gmail}')
        print(f'aceita outlook: {aceita_outlook}}')
        print(f'aceita yahoo: {aceita_yahoo}')
     

tela = TelaPython()
tela.Iniciar()        