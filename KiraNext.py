import os , requests , time ,json

try:
    arquivo = open("TOKEN.txt","r")
    TOKEN = arquivo.read()   
except:
    print("Nao foi possivel localizar o TOKEN")

URL = f"https://api.telegram.org/bot{TOKEN}"
resp = requests.get(f"{URL}/getUpdates").json()
msgJaRecebida = resp['result'][len(resp['result'])-1]['update_id']

ln = os.linesep   #esse comando esta servindo pra mim pula linha la no telegram
meuId = 1280346366

def recebeMsg():
    ultimamsg = resp['result'][len(resp['result'])-1]
    return ultimamsg['message']

def respondeUsuario(idUsuario,msg_p_usuario):
    '''responde o usuario; é nescessario seta os atributos: id e a mensagem '''
    requests.get(f"{URL}/sendMessage?chat_id={idUsuario}&text={msg_p_usuario}")

    return f"respondi = {msg_p_usuario}"



while(True):
    #Pegando todas as mensagens do bot  como esta dentro do while ele sempre puxa a atualizacao=====================
  
    resp = requests.get(f"{URL}/getUpdates").json()
#=======================================================
    
    utmBloco = len(resp['result'])-1
    
    chatId = resp['result'][utmBloco]['update_id']
    
    fromm = resp['result'][utmBloco]['message']['from']

    idUsuario = fromm['id']
    nomeUsuario = fromm['first_name']
    msgTxt = str(recebeMsg()['text']).lower()

    

    if msgJaRecebida !=  chatId:
        
        if msgTxt  == "/start":
            if idUsuario == meuId:  # essa parte so eu posso acessar tipo um acesso de ADMIN
                respondeUsuario(idUsuario,f"Bem vindo Mestre 😈")
                respondeUsuario(idUsuario,f"""
Deseja desliga seu computador digite /desliga {ln}
Cancelar o desligamento digite /cancelar       
                
                """)
                
            else:
                print(respondeUsuario(idUsuario,f"Bem vindo {nomeUsuario}"))
        
         

        #filtro dos comntarios   
        if msgTxt != "/start":
            if(msgTxt == "/desliga" and idUsuario == meuId ):
                    os.system('shutdown -s -t 160')
                    respondeUsuario(idUsuario,"desligamento em andamento")
            if(msgTxt == "/cancelar" and idUsuario == meuId):
                os.system("shutdown -a")
                respondeUsuario(idUsuario,"Desligamento cancelado")



        # comentario global
        respondeUsuario(idUsuario,"/setadoido") 

    msgJaRecebida = chatId
    time.sleep(1)
