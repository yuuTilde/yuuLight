import PySimpleGUI as sg
import os
from yeelight import Bulb
from tkinter import colorchooser

def main():
    sg.theme('Dark')
    #sg.SetOptions(icon='yuuTilde.ico')

    if not os.path.isfile('ip.txt'):
        with open('ip.txt', 'w') as f:
            f.close()
    with open('ip.txt', 'r') as f:
        ip = f.read()
        bulb = Bulb(ip)

    layout = [  [sg.Text("Bulb's IP"), sg.Input(default_text=(ip), size=(15)), sg.Button('Connect')],
                [sg.Button('On/Off'), sg.Button('Color'), sg.Button('Brightness'), sg.Text('0', key='brightness2')],
                [sg.Slider(range=(0,100), orientation='horizontal', disable_number_display=True, change_submits=True, key='brightness')],
                [sg.Text('yuutilde.github.io')]]

    window = sg.Window('yuuLight', layout, grab_anywhere=True, element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        window.Element('brightness2').Update(values['brightness'])
        if event == 'Connect':
            ip = values[0]
            with open('ip.txt', 'w') as f:
                f.write(ip)
            bulb = Bulb(ip)
        if event == 'On/Off':
            bulb.toggle()
        if event == 'Color':
            color = colorchooser.askcolor()
            bulb.set_rgb(color[0][0], color[0][1], color[0][2])
        if event == 'Brightness':
            brightness = values['brightness']
            bulb.set_brightness(brightness)

    window.close()

if __name__ == '__main__':
    main()