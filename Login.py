from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario',size=(35,1))],
    [sg.Text('Senha'), sg.Input(key='senha',password_char="*",size=(35,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout )

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'admin' and valores['senha'] == 'admin':
            print('Seja bem vindo ao programa Python')
            input()
            exit()
        else:
            print('usuário ou senha invalidos ! ')
