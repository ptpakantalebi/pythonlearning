a = input('enter the number: ')
if '^' in a:
    for x in range(0,len(a)):
        if a[x] == '^':
            p = a[0:x]
            h = a[x+1:len(a)]
            r = int(p)
            for yt in range(1,int(h)):
                r *= int(p)
    print(r)
import math
def isprime(e):
    iiu = 0
    for x in range(2,e):
        if e % x != 0:
            iiu += 1
    if iiu == e-2:
        return e
def real_prime_number(tyu):
    skfasd = 1
    while True:
        if (skfasd ** 2) <= tyu:
            if ((skfasd+1)**2) >= tyu:
                break
        skfasd += 1
    if math.sqrt(tyu) == skfasd ** 2:
        return
    if -1*((skfasd**2)-tyu) < (((skfasd+1)**2)-tyu):
        vnbsc = skfasd
    else:
        vnbsc = skfasd+1
    tesf = 0
    haripater = [x for x in range(2,vnbsc+1)]
    for lwkfj in haripater:
        if isprime(lwkfj):
            owe = 2
            while (lwkfj * owe) in haripater:
                haripater.remove(lwkfj * owe)
                owe += 1
    for tnt in haripater:
        if tyu % tnt != 0:
            tesf += 1
    if tesf == len(haripater):
        return tyu
if a.endswith('#'):
    er = 2
    for t in range(3,int(a[0:-1])+1,2):
        if real_prime_number(t):
            er *= t
    print(len(str(er)))
if a.endswith('!'):
    i = 1
    for q in range(2,int(a[0:-1])+1):
        i *= q
    print(i)