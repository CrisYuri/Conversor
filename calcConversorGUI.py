import PySimpleGUI as psg
import calcConversor

layout = [
    [psg.Text('Temperatura em Fahrenheit: '), psg.Input(key='Tf')],
    [psg.Text('', key='Valor')],
    [psg.Button('Calcular'), psg.Button('Limpar')]
       ]

janela = psg.Window('Conversor de Temperaturas V2.0', layout)

while True:
    eventos, valores = janela.read()
    if eventos == psg.WIN_CLOSED:
        break
    elif eventos == 'Limpar':
        janela['Tf'].update('')
        janela['Valor'].update('')
        janela['Tf'].set_focus()
    else:
        n1 = int(valores['Tf'])
        total = calcConversor.cel(n1)
        janela['Valor'].update(total)

janela.close()

