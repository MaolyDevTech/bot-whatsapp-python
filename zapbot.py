from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Olá! 🌟 Bem-vindo a novembro! 🍂 Este é o Zap Bot, seu assistente automatizado. Vamos tornar este mês incrível! 🚀, Aqui Maoly treinando automação"
        self.grupos = ["Grupo1", "Grupo2", "Grupo3"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
        

    def EnviarMensagens(self):
        # Aguarde o usuário escanear o código QR manualmente
        #input("Pressione Enter após escanear o código QR...")
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            grupo.click()
            time.sleep(3)
            chat_box = self.driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
            chat_box.click()
            time.sleep(3)
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()

