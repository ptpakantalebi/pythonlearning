a = input().split(' ')

while len(a) != 1:
    for b in range(0,3):
        d = 0
        for c in a:
            if b == 0:
                if a[d] == '*':
                    uuy = float(a[d-1])*float(a[d+1])                            
                    del a[d-1:d+2]
                    a.insert(d-1,str(uuy))
                    d -= 1
                if a[d] == '/':
                    uuy = float(a[d-1])/float(a[d+1])
                    del a[d-1:d+2]
                    a.insert(d-1,str(uuy))
                    d -= 1
            if b == 1:
                if a[d] == '+':
                    uuy = float(a[d-1])+float(a[d+1])
                    del a[d-1:d+2]
                    a.insert(d-1,str(uuy))
                    d -= 1
                if a[d] == '-':
                    uuy = float(a[d-1])-float(a[d+1])
                    del a[d-1:d+2]
                    a.insert(d-1,str(uuy))
                    d -= 1
            d += 1
print(a[0])