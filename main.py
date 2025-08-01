
import pandas as pd
import time
import pyautogui
import pyperclip
import webbrowser

df = pd.read_excel('placas.xlsx')
placas = df.iloc[:, 0].tolist()

url = 'https://forms.office.com/Pages/DesignPageV2.aspx?origin=NeoPortalPage&subpage=design&id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAMAAFFnA_5UQVdLTjgyNktZMzhVRjNDVEVWSDJKVlpXTy4u&branchingelementid=r55b7aeaf3942455e8905aac77ee79864'
webbrowser.open(url)

time.sleep(15)
pyautogui.press('tab', presses=16)
pyautogui.press('enter')
pyautogui.press('tab', presses=6)
pyautogui.press('tab')
pyautogui.press('enter')

for placa in placas:
    pyperclip.copy(str(placa))     
    pyautogui.hotkey('ctrl','v')  
    time.sleep(3)
    pyautogui.press('enter')