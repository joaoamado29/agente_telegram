import pyautogui as p
import time
import pyperclip

#1- Criar automação que recebe CNPJ, faz o web-scraping no site, e retorna o resultado obtido (em print, por enquanto)

# ---- Receber o CNPJ do usuário e trata a string -----------------------------
cnpj = input("Digite o CNPJ: ")
cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "").replace(" ", "")


# ---- Abre o Navegador e acessa o site da receita federal --------------------------------
p.press("win")
time.sleep(1)
p.write("chrome")
time.sleep(1)
p.press("enter")


# ---- Digitar CNPJ no campo de busca --------------------------------
time.sleep(2)
p.write("https://consopt.www8.receita.fazenda.gov.br/consultaoptantes")
p.press("enter")
time.sleep(3)


# ---- Selecionar o campo de busca e digitar o CNPJ --------------------------------
p.press("tab")
time.sleep(1)
p.write(cnpj, interval=0.1)
time.sleep(2)


# ---- Entrar no site e clicar em mais informações --------------------------------
p.press("enter")
time.sleep(2)
p.press("tab")
time.sleep(1)
p.press("enter")
time.sleep(2)

# ---- Selecionar e pegar informações do site --------------------------------
p.hotkey("ctrl", "a")
time.sleep(1)
p.hotkey("ctrl", "c")
time.sleep(1)

conteudo = pyperclip.paste()

# ---- Tratar o conteúdo copiado para extrair as informações desejadas --------------------------------
linhas = conteudo.split("\n")
print(linhas)

for i in linhas:
    print(i + '\n')

#2- Fazer o web-scraping no site da receita federal, usando o cnpj recebido

