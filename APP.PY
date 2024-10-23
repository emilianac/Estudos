from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import schedule

telefone = "XXXXXXXXXX" 
mensagem = f'XXXXXXXXXXX'

link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
webbrowser.open(link_mensagem_whatsapp)
sleep(10)
pyautogui.press('enter')  # Pressionar Enter
