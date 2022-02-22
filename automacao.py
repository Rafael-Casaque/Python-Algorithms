import time
import pyautogui as pg

time.sleep(5)

string = ['esta','mensagem','foi','escrita','e','enviada','utilizando','o','Python']

for i in string:    
    pg.write(i)
    pg.write(" ")
    time.sleep(0.5)
pg.press("enter")    