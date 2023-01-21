import pyautogui
import time
from selenium                          import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui     import WebDriverWait
from selenium.webdriver.support        import expected_conditions as EC
from selenium.webdriver.common.by      import By
from selenium.webdriver.common.keys    import Keys
from selenium.common.exceptions        import TimeoutException
from datetime                          import datetime, timedelta
from selenium.webdriver.chrome.options import Options
#pyinstaller --onefile



# Ir para área de trabalho
pyautogui.hotkey('winleft', 'd')

# Abrindo o browser 
Navegador = webdriver.Chrome()
time.sleep(2)
url = 
Navegador.get(url)
Navegador.maximize_window()
time.sleep(5)

# Logando a conta
# Email---
Email = 
pyautogui.click(1342, 91)
time.sleep(20)
Navegador.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/form/div[1]/div[1]/input').click()
pyautogui.write(Email)

# Senha---
Senha = 
time.sleep(1)
Navegador.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/form/div[2]/div[1]/input').click()
pyautogui.write(Senha)
Navegador.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/form/button').click()

# Abrindo o DashBoard
time.sleep(40)
pyautogui.click(285, 164)
time.sleep(5)
pyautogui.click(1342, 188)

# Redimesionando a tela
pyautogui.keyDown('ctrl')
pyautogui.scroll(-100)
pyautogui.scroll(-100)
time.sleep(1)
pyautogui.scroll(-100)
pyautogui.scroll(-100)
pyautogui.scroll(-100)
pyautogui.keyUp('ctrl')


# Tirando Print
while 1:
    #pyautogui.click(1342, 188)
    time.sleep(10)
    Print = Navegador.save_screenshot('C:/Users/douglas.felix/Desktop/Imagens/SAC-Print.png')
    #Navegador.refresh()
    time.sleep(40)
    
    
    
    
