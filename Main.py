import PySimpleGUI as sg
from QR_Gen import QRcoder


def main():


    layout = [
        [sg.Text('WiFi SSID', size=(15, 1)), sg.InputText("", key='ssid')],
        [sg.Text('Password', size=(15, 1)), sg.InputText("", key='password', password_char='*')],
        [sg.Text('Security Type', size=(15, 1)), sg.Combo(['WPA', 'WEP'], key='sec', size=(10,1))],
        [sg.Text('_' * 100, size=(65, 1))],
        [sg.Submit(), sg.Quit()]
    ]
    window = sg.Window('WiFi QR Code Generator', layout)

    while True:  # The Event Loop
        event, values = window.read()
        # print(event, values) #to uncomment debug
        if event in (None, 'Quit', 'Cancel'):
            break
        if event == 'Submit':

             try:
                QR = QRcoder(values['ssid'], values['password'], values['sec'])
                data = QR.wifi_qr_code()
                sg.popup(data)


             except Exception as e:
                sg.popup(e)


if __name__ == '__main__':
    main()
