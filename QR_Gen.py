import PySimpleGUI as sg
import pyqrcode as pq
import os

class QRcoder():
    def __init__(self, ssid, password, sec_type):

        self.ssid = ssid
        self.password = password
        self.sec_type = sec_type
        self.file_path = "c:/Temp"

    def qr_gen(self, ssid, password, sec_type):
        QR = pq.create(f'WIFI:S:{ssid};T:{sec_type};P:{password};;')
        return QR

    def default_path(self, file_path):
        os.chdir(file_path)

    def Window(self, file_path, img_name):

        layout = [
            [sg.Text(f'{self.ssid} WiFi', size=(15, 1), justification='center', font=('Arial', 15))],
            [sg.Image(f'{file_path}/{img_name}')],
            [sg.Multiline(default_text='open camara app to scan QR Code \n'
                                       'This allows you to connect\n'
                                       'to the Wifi', size=(35, 5))],

        ]
        window = sg.Window('QR Code', layout)

        return window

    def wifi_qr_code(self):
        self.default_path(self.file_path)
        QR = self.qr_gen(self.ssid, self.password, self.sec_type)
        image = f"{self.ssid}.png"
        QR.png(image, scale=7)
        display = self.Window(self.file_path, image)
        while True:
            event, value = display.read()
            if event in (None, 'Quit'):
                break







