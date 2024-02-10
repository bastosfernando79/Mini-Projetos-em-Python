from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.op.gg/champions/alistar/build')

# Encontrar a lista de jogadores
lista_players = driver.find_elements(By.CSS_SELECTOR, "a.summoner")

# Extrair o nome e o link de cada jogador
for player in lista_players:
    nome = player.text
    link = player.get_attribute("href")

    print(f"Nome: {nome}")
    print(f"Link: {link}")

driver.quit()
