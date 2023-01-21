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
email = "ti@atlas.ind.br"

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
key = '@g1l1d4d3'
Navegador.find_element_by_id("i0118").send_keys(key)
Navegador.find_element_by_id('idSIButton9').click()

# Pulando verificação Stay Signed in
time.sleep(2)
Navegador.find_element_by_xpath('//*[@id="KmsiCheckboxField"]').click()
Navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()

#####-------------------------------------------------------------------#######





# Abrindo pagina direto do painel, após logar na conta
time.sleep(4)
url_1 = "https://app.powerbi.com/groups/dbbcc9b3-7a69-4af2-9206-9fe495fd64f9/reports/812fb2fa-96ea-4aee-aeee-5483dc598e9f/ReportSection0736fec1036fd284ded6?chromeless=1"
Navegador.get(url_1)
Aba_1 = Navegador.current_window_handle


# Tirando Print
Print_1 = Navegador.save_screenshot('Qualidade-Geral.png')
while 1:
    time.sleep(5)
    Navegador.switch_to.window(Aba_1)
    time.sleep(5)
    Print_1 = Navegador.save_screenshot('Qualidade-Geral.png')
    
    Navegador.refresh()
    time.sleep(1200)
    



















