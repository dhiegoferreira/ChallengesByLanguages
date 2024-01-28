#Supermercado

N = int(input()) #número de supermercados
lista = []

for i in range(N): #Esse laço pega os valores da carne e a quantidade, em Quilograma, de seus respectivos Supermercados.
    valor = str(input())
    valores = valor.split()
    lista.append(float(valores[0]))
    lista.append(int(valores[1]))

listafinal =[]    
for i in range(len(lista)): #Faz cálculo o do valor de 1kg de carne dos preços de cada supermercado.
    if type(lista[i]) == float:
        listafinal.append((lista[i]*1000)/(lista[i+1]))
    
listafinal.sort() #Ordena a lista
print("{:.2f}".format(listafinal[0]))
