a = input().split(' ')
def math(n):
    while len(n) != 1:
        for b in range(0,3):
            d = 0
            for c in a:
                if b == 0:
                    if n[d] == '*':
                        uuy = float(n[d-1])*float(n[d+1])                            
                        del n[d-1:d+2]
                        a.insert(d-1,str(uuy))
                        d -= 1
                    if n[d] == '/':
                        uuy = float(n[d-1])/float(n[d+1])
                        del n[d-1:d+2]
                        n.insert(d-1,str(uuy))
                        d -= 1
                if b == 1:
                    if n[d] == '+':
                        uuy = float(n[d-1])+float(n[d+1])
                        del n[d-1:d+2]
                        n.insert(d-1,str(uuy))
                        d -= 1
                    if n[d] == '-':
                        uuy = float(n[d-1])-float(n[d+1])
                        del n[d-1:d+2]
                        n.insert(d-1,str(uuy))
                        d -= 1
                d += 1
    return n[0]
if '(' in a:
    list1 = []
    for members in range(0,len(a)):
        if a[members] == '(' or a[members] == ')':
            list1.append(members)
    while len(list1) != 0:
        print(math(a[list1[len(list1/2)-1]+1:list1[len(list1/2)]-1]))
        a.remove(list1[len(list1/2)-1])
        a.remove(list1[len(list1/2)])
        del list1[len(list1/2)-1:len(list1/2)]
else:
    print(math(a))