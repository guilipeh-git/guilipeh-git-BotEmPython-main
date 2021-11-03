def tiraAcento(texto) -> str:
    import unicodedata
    tiraAcentuacao = unicodedata.normalize("NFD",texto)
    return tiraAcentuacao.encode("ascii", "ignore").decode("utf-8").capitalize()

def formataTexto(texto):
    return" ".join(texto.split()).replace("> <","><")

def wikipedia(assunto):
    import requests
    from bs4 import BeautifulSoup as bs

    html = requests.get(f"https://pt.wikipedia.org/wiki/{tiraAcento(assunto)}").text
    
    html = formataTexto(html)
    soup = bs(html,"html.parser")
    soup = soup.decode("utf-8")
    soup = bs(html,"html.parser")
    texto = soup.find_all("p")

    def n(texto):
        if(len(texto)<= 7):
            return len(texto)
        return 7
        
    
    texto = [(texto[text].getText()) for text in range(1,n(texto))]
    return str(texto)[1:len(str(texto))-1]



if __name__ == "__main__":
    print(wikipedia("libra"))
    
    