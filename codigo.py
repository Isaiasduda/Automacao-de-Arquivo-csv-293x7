import pyautogui 
import time
import pandas as pd

pyautogui.Pause = 3

# ENTRA NO GOOGLE
pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

# ENTRA NO SITE
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

# CAMPO LOGIN
pyautogui.click(x=1007, y=556)
# pyautogui.hotkey("crtl" , "a")    #seleciona todo o texto que estiver dentro do campo 
pyautogui.write("duda.isaias@gmail.com")    
     
# PASSAR PARA O CAMPO SENHA 
pyautogui.press("tab")  # desce o cursor para o campo de inserir a senha
#pyautogui.click(x=964, y=747)
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter") 
# pyautogui.click(x=941, y=857)

time.sleep(1)

# IMPORTAR BASE DE DADOS
tabela = pd.read_csv("produtos.csv")

print(tabela)

pyautogui.Pause = 3 

# CADASTRAR PRODUTOS 
for linha in tabela.index:
    if linha == 10:
        break
    #codigo 
    pyautogui.click(x=802, y=421)
    codigo = str(tabela.loc[ linha, "codigo"])

    pyautogui.write(codigo)

    # marca
    pyautogui.press("tab")
    marca = str(tabela.loc[ linha, "marca" ]) 
    pyautogui.write(marca)

    # tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[ linha, "tipo" ]) 
    pyautogui.write(tipo)

    #categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[ linha, "categoria"])
    pyautogui.write("categoria")

    # preco_unitario
    pyautogui.press("tab")
    preco = str(tabela.loc[ linha, "preco_unitario" ])
    pyautogui.write(preco)

    #custo
    pyautogui.press("tab")
    custo = str(tabela.loc[ linha, "custo"])
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[ linha, "obs"])
    if obs != "nan":        
        
        pyautogui.write(obs)

    # CLICA NO BOTAO DE ENVIAR DEPOIS DE INSERIR TODOS OS PRODUTOS 

    pyautogui.press("tab")
    # pyautogui.click(x=864, y=418)#posicao do botao de enviar na tela
    pyautogui.press("enter")

    # SOBE A PAGINA PARA RETORNAR O LOOP E CONTINUAR A SEQUENCIA DE INSERÇÃO DE PRODUTOS
    pyautogui.scroll(1000)
    
    



