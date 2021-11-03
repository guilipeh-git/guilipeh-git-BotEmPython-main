import requests, json ,os ,signoGui,wikipediaGui
import cotacaoMoedaGui as moeda
from time import sleep





[r,w,g,y] = ["\033[31m","\033[m","\033[32m","\033[33m"] # tabela de cor 


try:
    arquivo = open("TOKEN.txt")
    token = arquivo.readline()
    arquivo.close()
    
except:
    print(f"{r}[ERRO]{w} ao abrir arquivo do TOKEN")
API = f"https://api.telegram.org/bot{token}/getUpdates"

print(API)
def contentFun(API):
    content = requests.get(API).json()

    teste = len(content["result"])
    if(teste != 0): 
        return requests.get(API).json()
    return {'ok': True, 'result': [{"update_id":"0","message":{"from":{"id":""},"text":" "}}]}

content = contentFun(API)

msgExistente = content['result'][-1]['update_id']

pl = os.linesep  # pula linha no telegram 

def menu():
    return f"""

/CursoIngles - link do curso grátis de inglês\n
/moeda - Cotação da moeda em tempo real \n
/signo - digite seu signo  \n
digite: /oquee e a palavra  que deseja pesquisar \n

            """




while True:
    
    content = contentFun(API)
    message = content['result'][-1]['message']
    from_ = message["from"]
    idUsuario = from_['id']
    ultimaMsg = content['result'][-1]['update_id']

    if(str(content["result"][-1]).find("text") != -1 and str(content["result"][-1]).find("reply_to_message") == -1):
        msgTxt = message['text'].lower()
    else:
        msgTxt = "Nao é uma message"
    
    responderUsuario = lambda msg , id=idUsuario : requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={msg}")

    if int(msgExistente) != int(ultimaMsg):
        if(msgTxt == "/start"): 
            responderUsuario(f"Olá {from_['first_name']}, Sejá bem vindo!!!")

        if(msgTxt.find("/moeda") != -1):
            responderUsuario(f"processando...")
            responderUsuario(moeda.moedaCotacao()) 
        
        if msgTxt.find("/signo") != -1:
            signo = msgTxt.replace("/signo","").strip()
            if len(signo) == 0:
                responderUsuario(f"[Erro] É necessario que você informe o signo.{pl}Ex:/signo sagitário")
            else:
                responderUsuario(f"processando...")
                responderUsuario(f"{signoGui.signo(signo)}")
        if(msgTxt == "/terminal"):
            responderUsuario("matando terminal do bot ...")
            os.system("tskill powershell")    
        if msgTxt.find("/shutdown") != -1:
            time = msgTxt.replace("/shutdown","").strip()

            def msgfun(time): 
                if (str(time).isnumeric()):
                    return "desligamento em andamento..."
                else:
                    return "Valor não aceito"
            responderUsuario(msgfun(time))
            os.system(f"shutdown -s -t {time or 160}")
        if msgTxt == "/cancelar":
            responderUsuario("desligamento cancelado...")
            os.system("shutdown -a")


        if msgTxt.find("/oquee") != -1:
            frase = msgTxt.replace("/oquee","")
            if len(frase) == 0:
                responderUsuario("campo invalido!!! digite: /oquee e a palavra(frase) que vc deseja pesquisar.")
            else:
                responderUsuario("aguarde só um momento ...")
                responderUsuario(wikipediaGui.wikipedia(frase))

        if msgTxt == "/cursoingles":
            responderUsuario("https://kultivi.com/cursos/idiomas/ingles")
        responderUsuario(menu())
        print(f"Mensagem {idUsuario} = {msgTxt}")

    
    
    
    
    
    
    
    msgExistente = ultimaMsg
    
        

#os.system("tskill powershell") # mata terminal 