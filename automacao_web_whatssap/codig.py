from selenium import webdriver
import time
import pyautogui as pya
import pyperclip

class WhatssapBot:
    def __init__(self):
        self.mensagem = "digite aqui a sua mensgem"

        self.contatos = ["nome dos seus grupo ou contatos"]

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMessagens(self):
        i = 0;
        self.driver.get('https://web.whatsapp.com/')
        while len(self.driver.find_elements_by_id("side")) < 1:
            time.sleep(3)

        for contato in self.contatos:
            contato = self.driver.find_element_by_class_name('_13NKt')
            contato.click()
            time.sleep(3)
            pya.write(self.contatos[i])
            time.sleep(2)
            pya.press("enter")

#             chat_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
#             time.sleep(3)
#            pya.click(596,677) #click caixa de texto
#             chat_box.click()
            time.sleep(3)
            pyperclip.copy(self.mensagem)
            pya.hotkey('ctrl','v')
            time.sleep(6)
            pya.press('enter')
            i += 1;

bot = WhatssapBot()
bot.EnviarMessagens()