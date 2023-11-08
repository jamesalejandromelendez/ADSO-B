from io import open
# -*- coding: utf-8 -*-
import pandas as pd
import pyautogui as pg
import webbrowser as web
import time

data = pd.read_excel("C:/Users/Andres/Desktop/contactos.xlsx")

#data = pd.read_excel(r"C:\Users\Andres\Desktop\contactos.xlsx")


for i in range (len(data)):
    celular = str(data.loc[i, 'celular'])
    nombre = data.loc[i,'nombre']

    #mensaje personalizado
    mensaje = 'Hola '+ nombre + ' !Gracias por comprar '

    #abrir navegador
    web.open("https://web.whatsapp.com/send?phone=" + celular+ '&text=' + mensaje)

    # enviar mensaje
    time.sleep(5)
    pg.click(1230,964)
    time.sleep(1)
    pg.press('enter')

    # cerrar pestaña
    time.sleep(1.5)
    pg.hotkey('ctrl', 'w')
    time.sleep(1)

