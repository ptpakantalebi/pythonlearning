a = input().split(' ')
for b in range(0,2):
    d = 0
    for c in a:
        if b == 0:
            if a[d] == '*':
                uuy = int(a[d-1])*int(a[d+1])
                del a[d-1:d+2]
                a.insert(d-1,str(uuy))
            if a[d] == '/':
                uuy = int(a[d-1])/int(a[d+1])
                del a[d-1:d+2]
                a.insert(d-1,str(uuy))
        if b == 1:
            if a[d] == '+':
                uuy = int(a[d-1])+int(a[d+1])
                del a[d-1:d+2]
                a.insert(d-1,str(uuy))
            if a[d] == '-':
                uuy = int(a[d-1])-int(a[d+1])
                del a[d-1:d+2]
                a.insert(d-1,str(uuy))
        d += 1
print(a)