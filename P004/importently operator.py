a = input().split(' ')
q = ['*','/','+','-']
for b in range(0,4):
    for x in range(0,len(a)):
        if a[x] == q[0] and q[b] == q[0]:
            a.insert(x-2,int(a[x-1])*int(a[x+1]))
            del a[int(a[x-1]):int(a[x+1])]
        if a[x] == q[1] and q[b] == q[1]:
            a.insert(x-2,int(a[x-1])/int(a[x+1]))
            del a[int(a[x-1]):int(a[x+1])]
        if a[x] == q[2] and q[b] == q[2]:
            a.insert(x-2,int(a[x-1])+int(a[x+1]))
            del a[int(a[x-1]):int(a[x+1])]
        if a[x] == q[3] and q[b] == q[3]:
            a.insert(x-2,int(a[x-1])-int(a[x+1]))
            del a[int(a[x-1]):int(a[x+1])]