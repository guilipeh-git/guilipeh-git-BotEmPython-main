import unicodedata

def retiraAcento(frase) -> str:
    normalized = unicodedata.normalize("NFD",frase)
    return normalized.encode("ascii", "ignore").decode("utf8").casefold()
#===============================================================================
def signo(signoUser="sagitario"):
    import requests, os
    from bs4 import BeautifulSoup as BS
    
    lista = """
    aries 
    touro 
    gemeos 
    Cancer 
    Leao 
    Virgem 
    Libra
    Escorpiao 
    Sagitario 
    Capricornio
    Aquario
    peixes """.lower()
    
    signoUser = retiraAcento(signoUser)
    if lista.find(signoUser) == -1:
       return f"[ERRO] signo {signoUser.title()} não existe"
    [pl] = [os.linesep]
    URL = requests.get(f"https://joaobidu.com.br/horoscopo/signos/previsao-{signoUser}/").text
    
    formata = lambda html : " ".join(html.split()).replace("> <","><")
    URL = formata(URL)

    soup = BS(URL,"html.parser")
    data = soup.findAll("div", class_ = "data")[-1].getText()
    texto = f"""{soup("p")[0].getText()}"""
    
    return f"""Horóscopo do dia {data}{pl}{pl}{signoUser}{pl}{pl}{texto}"""


if __name__ == "__main__":
    print(signo())