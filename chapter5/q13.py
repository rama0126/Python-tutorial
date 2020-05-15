import random
a=set([])
while True:
    a.add(random.randint(1,45))
    if len(a)==6:
        break
b = list(a)
b.sort()
print(b)