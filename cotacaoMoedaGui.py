def moedaCotacao():
    import requests,os

    # https://docs.awesomeapi.com.br/
    URL = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()

    moeda = lambda nomeMoeda,referenc: f"1 {nomeMoeda:<13} = R${float(URL[referenc]['bid']):.3f} {os.linesep}"

    #print(URL)
    return f"""{moeda("Dólar(EUA)","USDBRL")}{moeda("Euro(EUR)","EURBRL")}{moeda("Bitcoin(BTC)","BTCBRL")}
     """
    

#print(moedaCotacao())