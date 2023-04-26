from time import sleep
import datetime
import pyautogui, sys
import pyautogui
from time import sleep
import os

#String HORA ATUAL
data_atual = datetime.datetime.now()
#String dia atual
hoje = datetime.datetime.today()
#String Dia mes e ano atual
hoje_formatado = hoje.strftime('%d/%m/%Y')

#Alerta não mexer em nada!
pyautogui.alert('O Boot Tacob vai começar, não mexa !!')
pyautogui.PAUSE = 2

#1° Abrir o site da tacob
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.PAUSE = 2
pyautogui.write('https://tacob.adminml.com/login')
pyautogui.press('enter')

pyautogui.click(1026,315,duration=1)
pyautogui.write('rodrigo@link.com')  
pyautogui.click(966,415,duration=1)
pyautogui.write('!@#ControlDesk23')
pyautogui.press('enter')

#4° - clicar em tableros
pyautogui.click(903,303,duration=1.5)
#5° - clicar em %collections efficience
pyautogui.click(228,375,duration=3.5)
pyautogui.click(585,367,duration=3.5)

#6° - Selecionar opções desejadas
#DNR
pyautogui.click(328,141,duration=0.5)
#DNR
pyautogui.click(381,141)
#DNR
pyautogui.click(402,142)
#FATI
pyautogui.click(444,145)
#FATI   
pyautogui.click(484,146)
#FLEX
pyautogui.click(518,146)
#GRB
pyautogui.click(760,144)
#KITE
pyautogui.click(785,148)
#KITE
pyautogui.click(824,147)
#LEAL
pyautogui.click(859,148)
#LINK
pyautogui.click(914,140)
#NOV
pyautogui.click(988,145)
#QUIT
pyautogui.click(1147,137)
#TEST
pyautogui.click(1227,144)
#TOLI
pyautogui.click(1307,139)
#WFA
pyautogui.click(1341,139)
# - Clicar na seta de seleção de download (Consumer)
pyautogui.click(1314,267)#Botao Download
pyautogui.click(1347,311)#Botão Download


dir = '/Downloads'
old_file = os.path.join(dir, '% CE x AGENCIA - Tableros para Agencias - Gest Cli - INC.xlsx')
new_file = os.path.join(dir, hoje_formatado)
os.rename(old_file, new_file)

#DESCOBRIR CODIGO PARA RENOMEAR ARQUIVOS DO EXCEL, REFERENTE AO DIA EM QUE FEZ O DOWNLOAD
