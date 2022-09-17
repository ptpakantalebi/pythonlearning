a = input('enter the txt: ')
b = list(a)
list1 = []
r = 0
u = 0
w = [',','.','!','?']
for x in range(0,len(b)):
    if b[x] in w:
        u += ((x-1)-u)
        list1.append((r,u))
        r += ((x+2)-r)
    if b[x] == ' ':
        if b[x-1] not in w:
            u += ((x-1)-u)
            list1.append((r,u))
            r += ((x+1)-r)
c = list(map(lambda item:(b[item[0]:item[1]+1],item[0],item[1]+1),list1))
print(b)
print(c)
while True:
    f = input('enter the word: ')
    if f == 'END':
        break
    for p in c:
        if f == ''.join(p[0]):
            for yt in range(0,1):
                del b[p[1]:p[2]]
print(*b,sep='')