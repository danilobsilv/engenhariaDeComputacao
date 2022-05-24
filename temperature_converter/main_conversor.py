from interface.interfaces import *

janela1, janela2, janela3, janela4, janela5 = main_menu(), None, None, None, None

while True:
    janela, evento, valor = sg.read_all_windows()

    # janela 1
    if janela == janela1 and evento == sg.WIN_CLOSED:
        break
    if janela == janela1 and evento == "celsius":
        janela2 = temp_celsius()
        janela1.hide()
    if janela == janela1 and evento == "fahrenheit":
        janela3 = temp_fahrenheit()
        janela1.hide()
    if janela == janela1 and evento == "kelvin":
        janela4 = temp_kelvin()
        janela1.hide()
    if janela == janela1 and evento == "rankine":
        janela5 = temp_rankine()
        janela1.hide()
    if janela == janela1 and evento == "Fechar":
        break

    # janela 2
    if janela == janela2 and evento == sg.WIN_CLOSED:
        break
    if janela == janela2 and evento == "Ok":
        break
    if janela == janela2 and evento == "Voltar":
        janela2.hide()
        janela1.un_hide()
    if janela == janela2 and evento == "Converter":
        convertCel1 = float(valor["tempCel"]) * 1.8 + 32
        convertCel2 = float(valor["tempCel"]) + 273.15
        convertCel3 = float(valor["tempCel"]) * 9/5 + 491.67
        janela2["output1"].update(round(convertCel1, 1))
        janela2["output2"].update(round(convertCel2, 1))
        janela2["output3"].update(round(convertCel3, 1))

    # janela 3
    if janela == janela3 and evento == sg.WIN_CLOSED:
        break
    if janela == janela3 and evento == "Ok":
        break
    if janela == janela3 and evento == "Voltar":
        janela3.hide()
        janela1.un_hide()
    if janela == janela3 and evento == "Converter":
        convertFah1 = (float(valor["tempFah"]) - 32) / (5 / 9 + 273)
        convertFah2 = (float(valor["tempFah"]) - 32) * 5 / 9 + 273
        convertFah3 = float(valor["tempFah"]) + 459.67
        janela3["output1"].update(round(convertFah1, 1))
        janela3["output2"].update(round(convertFah2, 1))
        janela3["output3"].update(round(convertFah3, 1))

    # janela 4
    if janela == janela4 and evento == sg.WIN_CLOSED:
        break
    if janela == janela4 and evento == "Ok":
        break
    if janela == janela4 and evento == "Voltar":
        janela4.hide()
        janela1.un_hide()
    if janela == janela4 and evento == "Converter":
        convertKel1 = (float(valor["tempKel"])) - 273
        convertKel2 = (float(valor["tempKel"]) - 273) * 1.8 + 32
        convertKel3 = float(valor["tempKel"]) * 1.8
        janela4["output1"].update(round(convertKel1, 1))
        janela4["output2"].update(round(convertKel2, 2))
        janela4["output3"].update(round(convertKel3, 1))

    # janela 5
    if janela == janela5 and evento == sg.WIN_CLOSED:
        break
    if janela == janela5 and evento == "Ok":
        break
    if janela == janela5 and evento == "Voltar":
        janela5.hide()
        janela1.un_hide()
    if janela == janela5 and evento == "Converter":
        convertRank1 = (float(valor["tempRan"]) - 491.67) * 5/9
        convertRank2 = float(valor["tempRan"]) - 459.67
        convertRank3 = float(valor["tempRan"]) * 5/9
        janela5["output1"].update(round(convertRank1, 1))
        janela5["output2"].update(round(convertRank2, 1))
        janela5["output3"].update(round(convertRank3, 1))
