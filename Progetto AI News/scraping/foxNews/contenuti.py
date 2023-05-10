import requests, bs4
import pandas as pd

FILE_NAME = "foxNews/nuovi_link.csv"
DATABASE_NAME = "./database.csv"

df = pd.read_csv(FILE_NAME)
link_listaDiListe = df.values.tolist()


for link in link_listaDiListe:
    response = requests.get(link[0])
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    div_data = soup.find("div", class_ = "article-date")
    data = div_data.get_text()

    div_articolo = soup.find("div", {"class" : "article-body"})
    corpo_articolo = div_articolo.get_text()

    h1_titolo = soup.find("h1", {"class" : "headline"})
    titolo = h1_titolo.get_text()

    dati = [link[0],titolo, corpo_articolo, data]

    df = pd.DataFrame(data = [dati])
    df.to_csv(DATABASE_NAME, index=False, header=False, mode="a", sep="\t", encoding='utf-8')
