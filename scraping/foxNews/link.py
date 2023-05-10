import bs4
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def is_csv_empty(file_path):
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            return True
        else:
            return False
    except pd.errors.EmptyDataError:
        return True

def isOld(elemento, listaDiliste):
    for x in listaDiliste:
        if elemento in x:
            return True
    return False

LINK = "https://www.foxnews.com/search-results/search?q=artificial%20intelligence"
FILE_LINK = "foxNews/link.csv"
FILE_NUOVILINK = "foxNews/nuovi_link.csv"

options = Options()
options.headless = True  # Esegui il browser in modalità headless

# Avvia il browser
driver = webdriver.Chrome(options=options)

# Effettua la richiesta HTTP alla pagina web
driver.get(LINK)

# Ottieni il contenuto HTML aggiornato
html = driver.page_source

soup = bs4.BeautifulSoup(html, "html.parser")
articoli = soup.find_all("article", class_="article")
driver.quit()

listaLinks = []
for articolo in articoli:
    h2_notizie = articolo.find("h2", class_ = "title")
    a_notizie = h2_notizie.find("a")
    link = str(a_notizie.get("href"))
    if link not in listaLinks:
        listaLinks.append(link) 

nuovi_link = []
if is_csv_empty(FILE_LINK):
    df = pd.DataFrame(listaLinks)
    df.to_csv(FILE_LINK, index= False, mode="a", sep="\t", encoding='utf-8')
    df.to_csv(FILE_NUOVILINK, index= False, mode="a", sep="\t", encoding='utf-8') 
else:
    df = pd.read_csv(FILE_LINK)
    vecchi_link = df.values.tolist()
    for el in listaLinks:
        if isOld(el, vecchi_link) == False:
            nuovi_link.append(el)
    df = pd.DataFrame(nuovi_link)
    df.to_csv(FILE_LINK, index= False, mode="a", sep="\t", encoding='utf-8')    
    df.to_csv(FILE_NUOVILINK, index= False, mode="a", sep="\t", encoding='utf-8') 
