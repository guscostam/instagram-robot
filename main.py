from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PySimpleGUI import PySimpleGUI as sg
from time import sleep

#Layout
sg.theme('LightGrey1')
layout = [
    [sg.Text('Usuario Instagram'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Text('Hashtag do Nicho'), sg.Input(key='hashtag')],
    [sg.Text('Número de Postagens Curtidas (Apenas Números)'), sg.Input(key='likes')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('InstagramBot By: Gustavo Margotti', layout)

#Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        webdriver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        sleep(2)
        webdriver.get('https://www.instagram.com')
        sleep(2)

        usuario = webdriver.find_element_by_name('username')
        usuario.send_keys(valores['usuario'])
        sleep(1)
        senha = webdriver.find_element_by_name('password')
        senha.send_keys(valores['senha'])
        sleep(1)

        botao_login = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        botao_login.click()
        sleep(3)

        agora_nao = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        agora_nao.click()
        sleep(2)

        webdriver.get('https://www.instagram.com/explore/tags/' + valores['hashtag'] + '/')
        sleep(2)
        primeira_thumb = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]')
        primeira_thumb.click()
        sleep(2)

        webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
        sleep(2)

        webdriver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/button').click()
        sleep(3)

        for _ in range(1, int(valores['likes'])):
            botao_like = webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            botao_like.click()
            sleep(3)
                
            webdriver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/button').click()
            sleep(2)

    janela.close()
