vogais = ['a','e','i','o','u']
palavra = str(input())
palavra = list(palavra.lower())
for i in range(len(palavra)):
    for j in range(len(vogais)):
        if(palavra[i] == vogais[j]):
            palavra[i] = palavra[i].upper()
            
print(''.join(palavra))
print(''.join(teste))
