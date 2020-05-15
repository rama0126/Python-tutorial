import random
j=0
k=[]
while j<6:
    i = random.randint(1,45)
    if i in k:continue
    k.append(i)
    j+=1
k.sort()
print(k)