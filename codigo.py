# _*_ coding: utf-8 _*_

import pyautogui
import pyperclip
import time
import pandas as pd

tabela = pd.read_csv("clientes.csv")

# Ajustar o intervalo entre os comandos do PyAutoGUI
pyautogui.PAUSE = 0.6

# Caminho absoluto para o arquivo de texto
caminho_arquivo = r"C:\python\imóveis\RPA_Python_csv\clientes.csv"

# Lista para armazenar os números de WhatsApp
print(tabela)

# Passo 4: inserir um whats
with open(caminho_arquivo, 'r', encoding='ISO-8859-1') as arquivo:
    for linha in tabela.index:
    # clicar no campo de código
        pyautogui.click(x=320, y=174)

        # pegar da tabela o valor do campo que a gente quer preencher
        codigo = tabela.loc[linha, "codigo"]
        # preencher o campo
        pyautogui.write(str(codigo))
        
        # Pressionar Enter para buscar o contato
        pyautogui.press("enter")
        
        # Aguardar 2 segundos para garantir que a busca foi concluída
        time.sleep(2.0)

        # Clicar na barra de conversa
        pyautogui.click(x=1100, y=973)
        
        # Mensagem a ser enviada
        mensagem = '''Olá, Bom dia e BOA SEMANA!! 😃🙏

*JÁ VISITOU UM APARTAMENTO DECORADO?*

    Sou o *Rodolfo*, Consultor *SETE 7* pela Imobiliária Abyara. Dedicado em *realizar sonhos há mais de 10 anos!*

📍Há interesse em adquirir apartamentos na planta, seja do projeto *"Minha Casa, Minha Vida"*, de *Médio* ou *Alto padrão*?

 ✅ O financiamento pela *Caixa*, possui subsídios disponíveis para oferecer melhor *taxa de juros*.

🎯 Informe *pontos de interesse* como: *região, dormitórios, vagas na garagem, suíte ou itens de lazer* que te mando as opções!
    

🆙 Podemos *agendar* uma visita em um dos nossos *empreendimentos* para conversarmos melhor?
                   
      *Estou disponível para qualquer informação.* Tudo de bom!! 🙌😃
      
      @rodocs7
      @abyarabrokers
      Cel: 11 98122-0983 (whats)'''
        
        # Copiar a mensagem para a área de transferência
        pyperclip.copy(mensagem)
        
        # Colar a mensagem na barra de conversa
        pyautogui.hotkey('ctrl', 'v')
        
        # Descomente a linha abaixo se quiser enviar a mensagem automaticamente
        # pyautogui.press('enter')

        pyautogui.hotkey('win', 'e')
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'l')
        caminho = r'C:\python\imóveis\RPA_Python_csv\imagem'  # Usando string raw
        pyperclip.copy(caminho)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'c')  # Copia imagens
        time.sleep(.01)
        pyautogui.hotkey('alt', 'f4')
        pyautogui.click(x=1100, y=973)  # Barra de conversa
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1.5)
        pyautogui.press('enter')