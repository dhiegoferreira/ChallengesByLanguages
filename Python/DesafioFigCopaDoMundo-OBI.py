#Figurinhas da copa


linha1 = str(input())
linha1Split = linha1.split()

N = int(linha1Split[0]) #Quantidade de espaços
C = int(linha1Split[1]) #N° de figurinhas carimbadas
M = int(linha1Split[2]) #N°de fig compradas

figcompradas = []
figcarimbadas = []
semrep = []
qtdsemca = 0

linha2 = str(input())
linha2Split = linha2.split()
for i in range(C):
    figcarimbadas.append(linha2Split[i])






#Lista de figurinhas compradas
linha3 = str(input())
linha3Split = linha3.split()

for i in range(M):
    figcompradas.append(linha3Split[i])



print(figcompradas)

##Tirando as repetidas
for i in figcompradas:
        if i not in semrep:
            semrep.append(i)


print(semrep)

#Contando quantas carimbadas
for i in semrep:
    for j in figcarimbadas:
        if(i == j):
            qtdsemca += 1

        
        

print(qtdsemca)
