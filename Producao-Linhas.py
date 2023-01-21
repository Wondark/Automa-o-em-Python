import pyautogui
import time
from selenium                          import webdriver
#import playwrite.sync_api
#pyinstaller --onefile

#Tempo de Inicializar
time.sleep(5)

#Ir para área de trabalho
pyautogui.hotkey('winleft', 'd')

#Abrindo o browser  -  ABA 1
Navegador = webdriver.Chrome()
time.sleep(5)

#Abrindo o Site do Power BI
url_1 = "https://powerbi.microsoft.com/pt-br/"
Navegador.get(url_1)
Navegador.maximize_window()
time.sleep(5)
original_window = Navegador.current_window_handle



#####---------------------------------------------------------------------#####
# ------   Logando na conta   ------
#       *****  Email  *****
email = 

Navegador.find_element_by_id("power-bi-portal-link-desktop").click()    #Botão entrar
time.sleep(10)

#------------------------------------------------------------------------------
#Verificando aba dupla - Microsoft FDP vive mudando isso
#Quando vai logar, abre outra ABA
i = 1
Aba_1 = Aba_2 = 0
for window in Navegador.window_handles:
    if window != original_window:
        Navegador.close()
        Navegador.switch_to.window(window)
        i += 1
#-----------------------------------------------------------------------------

Navegador.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]").send_keys(email)     #Campo de email
Navegador.find_element_by_id("idSIButton9").click()        #Botão avançar/logar

#Escolhendo o tipo de conta. OBS: É pedido nessa conta da TI
  #time.sleep(5)
#       ***** Senha *****
  #Navegador.find_element_by_id('aadTile').click()

time.sleep(5)
key = 
Navegador.find_element_by_id("i0118").send_keys(key)
Navegador.find_element_by_id('idSIButton9').click()

# Pulando verificação Stay Signed in
time.sleep(2)
Navegador.find_element_by_xpath('//*[@id="KmsiCheckboxField"]').click()
Navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()

#####-------------------------------------------------------------------#######





# Abrindo pagina direto do painel, após logar na conta
#-----------------------------------------------------
#Links de cada Linha
time.sleep(4)
url_1 = 
url_2 = 
url_3 = 
url_4 = 
url_5 = 
url_6 = 
url_CKD = 
url_COOK = 
url_FN =  


#Eliminando a Aba nova que o próprio site do Power BI abre
original_window = Navegador.current_window_handle
Navegador.execute_script("window.open()")

for window in Navegador.window_handles:
    if window != original_window:
        Navegador.close()
        Navegador.switch_to.window(window)

# Usando um for para abrir as 8 Abas, uma para cada linha
time.sleep(10)
for X in range(8):
    Navegador.execute_script("window.open()")
    time.sleep(3)



#Loop para atribuir cada aba a um endereço
i = 0
for window in Navegador.window_handles:
    if i == 0:
        Aba_1 = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_1)
        time.sleep(2)
        Navegador.get(url_1)
    if i == 1:
        Aba_2 = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_2)
        time.sleep(2)
        Navegador.get(url_2)
    if i == 2:
        Aba_3 = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_3)
        time.sleep(2)
        Navegador.get(url_3)
    if i == 3:
        Aba_4 = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_4)
        time.sleep(2)
        Navegador.get(url_4)
    if i == 4:
        Aba_5 = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_5)
        time.sleep(2)
        Navegador.get(url_5)
    if i == 5:
        Aba_6 = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_6)
        time.sleep(2)
        Navegador.get(url_6)
    if i == 6:
        Aba_CKD = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_CKD)
        time.sleep(2)
        Navegador.get(url_CKD)
    if i == 7:
        Aba_COOK = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_COOK)
        time.sleep(2)
        Navegador.get(url_COOK)
    if i == 8:
        Aba_FN = window
        time.sleep(3)
        Navegador.switch_to.window(Aba_FN)
        time.sleep(2)
        Navegador.get(url_FN)
        time.sleep(3)
        Navegador.refresh()
    i += 1




# Loop de repetição infinita 
#Auternando entre abas
while 1:
    time.sleep(3)
    Navegador.switch_to.window(Aba_1)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-01.png')

    time.sleep(3)
    Navegador.switch_to.window(Aba_2)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-02.png')

    time.sleep(3)
    Navegador.switch_to.window(Aba_3)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-03.png')

    time.sleep(3)
    Navegador.switch_to.window(Aba_4)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-04.png')
    
    time.sleep(3)
    Navegador.switch_to.window(Aba_5)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-05.png')

    time.sleep(3)
    Navegador.switch_to.window(Aba_6)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-06.png')
    
    time.sleep(3)
    Navegador.switch_to.window(Aba_CKD)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-CKD.png')

    time.sleep(3)
    Navegador.switch_to.window(Aba_COOK)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-COOK.png')

    time.sleep(3)
    Navegador.switch_to.window(Aba_FN)
    time.sleep(8)
    Navegador.save_screenshot('LINHA-FN.png')
    
    time.sleep(180)














