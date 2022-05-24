from PySimpleGUI import PySimpleGUI as sg
#  [sg.Text("Celsius:"), sg.Button(key="celsius", size=(5, 1), pad=(20, 10), )],


def main_menu():
    sg.theme("DarkGreen")

    layout = [
        [sg.Text("Escolha a escala de entrada:", font="Verdana")],

        [sg.Button(key="celsius", button_text="CELSIUS", size=(10, 3), pad=(85, 7))],

        [sg.Button(key="fahrenheit", button_text="FAHRENHEIT", size=(10, 3), pad=(85, 7))],

        [sg.Button(key="kelvin", button_text="KELVIN", size=(10, 3), pad=(85, 7))],

        [sg.Button(key="rankine", button_text="RANKINE", size=(10, 3), pad=(85, 7))],

        [sg.Button("Fechar", pad=(103, 7))]
    ]

    return sg.Window("Menu de escolha", layout=layout, finalize=True)


def temp_celsius():
    sg.theme("DarkGreen")

    layout = [
        [sg.Text("Insira a temperatura em Celsius:"), sg.Input(key="tempCel", size=5)],

        [sg.Text("Em Fahrenheit:"), sg.Text(size=(20, 1), key="output1")],

        [sg.Text("Em Kelvin:"), sg.Text(size=(20, 1), key="output2")],

        [sg.Text("Em Rankine:"), sg.Text(size=(20, 1), key="output3")],

        [sg.Button("Converter"), sg.Button("Voltar"), sg.Button("Ok")]
    ]

    return sg.Window("Celsius", layout=layout, finalize=True)


def temp_fahrenheit():
    sg.theme("DarkGreen")

    layout = [
        [sg.Text("Insira a temperatura em Fahrenheit:"), sg.Input(key="tempFah", size=5)],

        [sg.Text("Em Celsius:"), sg.Text(size=(20, 1), key="output1")],

        [sg.Text("Em Kelvin:"), sg.Text(size=(20, 1), key="output2")],

        [sg.Text("Em Rankine:"), sg.Text(size=(20, 1), key="output3")],

        [sg.Button("Converter"), sg.Button("Voltar"), sg.Button("Ok")]
    ]

    return sg.Window("Fahrenheit", layout=layout, finalize=True)


def temp_kelvin():
    sg.theme("DarkGreen")

    layout = [
        [sg.Text("Insira a temperatura em Kelvin:"), sg.Input(key="tempKel", size=5)],

        [sg.Text("Em Celsius:"), sg.Text(size=(20, 1), key="output1")],

        [sg.Text("Em Fahrenheit:"), sg.Text(size=(20, 1), key="output2")],

        [sg.Text("Em Rankine:"), sg.Text(size=(20, 1), key="output3")],

        [sg.Button("Converter"), sg.Button("Voltar"), sg.Button("Ok")]
    ]

    return sg.Window("Kelvin", layout=layout, finalize=True)


def temp_rankine():
    sg.theme("DarkGreen")

    layout = [
        [sg.Text("Insira a temperatura em Rankine:"), sg.Input(key="tempRan", size=5)],

        [sg.Text("Em Celsius:"), sg.Text(size=(20, 1), key="output1")],

        [sg.Text("Em Fahrenheit:"), sg.Text(size=(20, 1), key="output2")],

        [sg.Text("Em Kelvin:"), sg.Text(size=(20, 1), key="output3")],

        [sg.Button("Converter"), sg.Button("Voltar"), sg.Button("Ok")]
    ]

    return sg.Window("Rankine", layout=layout, finalize=True)
