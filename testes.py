lista = ["pedro","guilherme",'maria',"joao","julia","maicon"]
filtro =  lambda nome: print(f"{nome[:2]}{nome[2:3].upper()}{nome[3:]}")
[filtro(nome) for nome in lista]


