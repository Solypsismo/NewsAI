import requests, bs4
import pandas as pd

FILE_NAME = "corriereDellaSera/nuovi_link.csv"
DATABASE_NAME = "./database.csv"

def is_csv_empty(file_path):
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            return True
        else:
            return False
    except pd.errors.EmptyDataError:
        return True

df = pd.read_csv(FILE_NAME)
listaLink = df.values.tolist()

corpo_Articolo = ""

for link in listaLink:
    response = requests.get(link[0])
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    h1_titolo = soup.find("h1", {"class": "title-art-hp is-xmedium is-line-h-106 is-mr-b-20"})
    if h1_titolo == None:
        continue
    else:
        titolo = h1_titolo.get_text()

    div_articolo = soup.find("div", {"class": "content"})
    
    if div_articolo == None:
        continue
    corpo_Articolo = div_articolo.get_text()

    p_data = soup.find("p", class_ = "is-last-update") 
     
    if p_data == None:
        continue
    else:
        data = str(p_data.get_text("p")).strip()

    dati = [link[0], titolo, corpo_Articolo, data] 
    df = pd.DataFrame(data = [dati])
    df.to_csv(DATABASE_NAME, index=False,header=False, mode='a', sep='\t')



