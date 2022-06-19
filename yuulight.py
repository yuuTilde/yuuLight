import PySimpleGUI as sg
from os import path
from yeelight import Bulb
from tkinter import colorchooser

def main():
    sg.theme('Dark')
    sg.SetOptions(icon='img/yuuLight.ico')

    if not path.isfile('ip.txt'):
        with open('ip.txt', 'w') as f:
            f.close()
    with open('ip.txt', 'r') as f:
        ip = f.read()
        bulb = Bulb(ip)

    layout = [  [sg.Text("Bulb's IP"), sg.Input(default_text=(ip), size=(15)), sg.Button('Connect')],
                [sg.Push(), sg.Button('On/Off'), sg.Button('Color'), sg.Push()],
                [sg.Slider(range=(0,100), orientation='horizontal', disable_number_display=True, change_submits=True, key='Brightness')],
                [sg.Text('Brightness:'), sg.Text('0', key='BrightnessText'), sg.Button('Apply', key='BrightnessApply')],
                [sg.Slider(range=(1700,6500), orientation='horizontal', disable_number_display=True, change_submits=True, key='Temperature')],
                [sg.Text('Temperature:'), sg.Text('0', key='TemperatureText'), sg.Button('Apply', key='TemperatureApply')],
                [sg.Text('yuutilde.github.io')]]

    window = sg.Window('yuuLight', layout, grab_anywhere=True, element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        window.Element('BrightnessText').Update(values['Brightness'])
        window.Element('TemperatureText').Update(values['Temperature'])
        if event == 'Connect':
            ip = values[0]
            with open('ip.txt', 'w') as f:
                f.write(ip)
            bulb = Bulb(ip)
        if event == 'On/Off':
            bulb.toggle()
        if event == 'Color':
            color = colorchooser.askcolor()
            if color[0] is not None:
                bulb.set_rgb(color[0][0], color[0][1], color[0][2])
        if event == 'BrightnessApply':
            bulb.set_brightness(values['Brightness'])
        if event == 'TemperatureApply':
            bulb.set_color_temp(values['Temperature'])
    window.close()

if __name__ == '__main__':
    main()