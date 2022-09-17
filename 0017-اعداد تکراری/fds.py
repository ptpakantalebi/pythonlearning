a = int(input('enter the number: '))
b = input()
c = b.split(' ')
list2 = []
list= []
for x in range(0,a-1):
    n = input()
    e = n.split(' ')
    list.append(e)
for i in range(0,len(c)):
    t = 0
    for u in list:
        if c[i] in u:
            t += 1
        if t+1 == a:
            if c[i] in list2:
                break
            list2.append(c[i])
print('output: ')
print(*list2,sep=' ')