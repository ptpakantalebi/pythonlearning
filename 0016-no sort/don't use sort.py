a = input('enter the numbers: ')
b = a.split(' ')[1:]
c = list(map(lambda d:int(d),b))
list_0 = []
while len(c):
    for d in c:
        f = 0
        for e in c:
            if d < e or d == e:
                f += 1
                if f == len(c):
                    list_0.append(d)
                    c.remove(d)
if a[0:3] == 'ACS':
    print(list_0)

if a[0:4] == 'DESC':
    print(list_0.reverse())