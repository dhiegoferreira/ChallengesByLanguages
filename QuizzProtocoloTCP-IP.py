import random 
vetsort = list()
pos = (1,2,3,4,5)
while len(vetsort) != 6:
        num = random.choice(pos)
        vetsort.append(num)
        aux = vetsort
        for ele in aux:
            repete = vetsort.count(ele)
            while repete != 1:
                vetsort.remove(ele)
                repete -= 1

print(vetsort)