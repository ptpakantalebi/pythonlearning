a = [b for b in range(3,int(input('enter the number: '))+1,2)]
for x in a:
    w = 3
    while x * w <= a[-1]:
        print(11)
        if x * w in a:
            print(111)
            a.remove(x*w)
        w += 2
print(2,*a,sep=' ')