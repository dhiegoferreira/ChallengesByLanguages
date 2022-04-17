HexaDecimal = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
Decimal = [0,1,2,3,4,5,6,7,8,9]


soma = 0;
N = int(input())
ListaMensagens = list(range(N))
ListaDecimais = list(range(N))

for i in range(N):
    Mensagem = str(input()).upper() [::-1]
    ListaMensagens[i] = Mensagem
    for j in range(len(Mensagem)):
        if(Mensagem[j] == 'A'):
            soma = ((10) * (16**j))
            ListaDecimais[i] += soma  
        elif(Mensagem[j] == 'B'):
            soma = ((11) * (16**j))
            ListaDecimais[i] += soma  
        elif(Mensagem[j] == 'C'):
            soma = ((12) * (16**j))
            ListaDecimais[i] += soma  
        elif(Mensagem[j] == 'D'):
            soma = ((13) * (16**j))
            ListaDecimais[i] += soma  
        elif(Mensagem[j] == 'E'):
            soma = ((14) * (16**j))
            ListaDecimais[i] += soma  
        elif(Mensagem[j] == 'F'):
            soma = ((15) * (16**j))
            ListaDecimais[i] += soma  
        else:
            soma = (int(Mensagem[j]) * (16**j))
            ListaDecimais[i] += soma  
    soma = 0

for k in ListaDecimais:
    print(k)
    
print(ListaMensagens)
print(ListaDecimais)
