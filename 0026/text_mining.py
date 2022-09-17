a = input('enter the number: ')
if '^' in a:
    tb = 1
    if 'x' in a:
        for o9 in a.split(' x '):
          for x in range(0,len(o9)):
            if o9[x] == '^':
                p = o9[0:x]
                h = o9[x+1:len(o9)]
                r = int(p)
                for yt in range(1,int(h)):
                    r *= int(p)
                tb *= r
    print(tb)
from functools import reduce
import math
from datetime import datetime
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
    tesf = 1
    haripater = [q for q in range(3,vnbsc+1,2)]
    for lwkfj in haripater:
            owe = 3
            while (lwkfj * owe) < haripater[-1]:
                if lwkfj * owe in haripater:
                    haripater.remove(lwkfj * owe)
                owe += 2
    for tnt in haripater:
        if tyu % tnt != 0:
            tesf += 1
    if tesf-1 == len(haripater):
        return tesf
if a.endswith('#'):
    er = 2
    for t in range(3,int(a[0:-1])+1,2):
        if real_prime_number(t):
            er *= t
    print(len(str(er)))
if a.endswith('!'):
    t0 = datetime.now()
    print()
    t1 = datetime.now()
    print(t1-t0)