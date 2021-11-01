
def raspaSite(URL):
    import requests
    from bs4 import BeautifulSoup as Beaut
    
    site = requests.get(URL).text
    formata = lambda html: " ".join(html.split()).replace("> <","><") # formata o html retirando \n \t e espaçamentos
    site = formata(site)

    soup = Beaut(site,"html.parser")
    #soup = soup.find(id="texto").get_text()
    resp = soup.body.get_text(separator = " guilherme ",strip=True)
    print(resp)
    print()



raspaSite('https://www.situacao-cadastral.com/')
