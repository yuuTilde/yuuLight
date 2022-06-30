import PySimpleGUIQt as sg
from os import path
from yeelight import Bulb


def main():
    sg.theme("Dark")
    # sg.SetOptions(icon="img/yuuLight.ico")

    if not path.isfile("ip.txt"):
        with open("ip.txt", "w") as f:
            f.close()
    with open("ip.txt", "r") as f:
        ip = f.read()
        bulb = Bulb(ip)

    layout = [
        [
            sg.Text("Bulb's IP"),
            sg.InputText(default_text=(ip)),
            sg.Button("Connect"),
        ],
        [
            sg.Button("On/Off"),
            sg.InputText(change_submits=True, key="ColorA", visible=False),
            sg.ColorChooserButton("Color", target="ColorA"),
        ],
        [
            sg.Slider(
                range=(0, 100),
                orientation="horizontal",
                change_submits=True,
                key="Brightness",
            )
        ],
        [
            sg.Text("Brightness:"),
            sg.Text("0", key="BrightnessText"),
            sg.Button("Apply", key="BrightnessApply"),
        ],
        [
            sg.Slider(
                range=(1700, 6500),
                orientation="horizontal",
                change_submits=True,
                key="Temperature",
            )
        ],
        [
            sg.Text("Temperature:"),
            sg.Text("0", key="TemperatureText"),
            sg.Button("Apply", key="TemperatureApply"),
        ],
        [sg.Text("yuutilde.github.io")],
    ]

    window = sg.Window(
        "yuuLight", layout, element_justification="center", resizable=False
    )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        window.Element("BrightnessText").Update(values["Brightness"])
        window.Element("TemperatureText").Update(values["Temperature"])
        if event == "Connect":
            ip = values[0]
            with open("ip.txt", "w") as f:
                f.write(ip)
            bulb = Bulb(ip)
        if event == "On/Off":
            bulb.toggle()
        if event == "ColorA":
            color = values["ColorA"]
            rgb = [int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)]
            if rgb[0] == 0 and rgb[1] == 0 and rgb[2] == 0:
                rgb = [255, 255, 255]
            bulb.set_rgb(*rgb)
        if event == "BrightnessApply":
            bulb.set_brightness(values["Brightness"])
        if event == "TemperatureApply":
            bulb.set_color_temp(values["Temperature"])
    window.close()


if __name__ == "__main__":
    main()
