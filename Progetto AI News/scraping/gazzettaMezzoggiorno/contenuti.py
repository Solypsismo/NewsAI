import requests, bs4
import pandas as pd

FILE_NAME = "gazzettaMezzoggiorno/nuovi_link.csv"
DATABASE_NAME = "./database.csv"

df = pd.read_csv(FILE_NAME)
listaLink = df.values.tolist()

corpo_Articolo = ""

for link in listaLink:
    
    response = requests.get(link[0])
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    
    h1_titolo = soup.find("h1", {"class" : "titolo_articolo titolo"})
    titolo = h1_titolo.get_text()

    p_data = soup.find("p", class_ = "data_articolo data") 
    data = str(p_data.get_text("p")).strip()
    
    div_articolo = soup.find("div", class_ = "testo_articolo testo testoResize")
    corpo_Articolo = div_articolo.get_text()

    dati = [link[0], titolo, corpo_Articolo.rstrip('\n'), data] 

    df = pd.DataFrame(data = [dati])
    df.to_csv(DATABASE_NAME, index=False,header=False, mode='a', sep='\t')   




