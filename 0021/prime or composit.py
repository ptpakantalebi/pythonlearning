a = int(input('enter the number: '))
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
if real_prime_number(a):
    print(a,'is a prime number.')
    er = 2
    for t in range(3,a+1,2):
        if real_prime_number(t):
            er *= t
    print(f'{a}# has {len(str(er))} decimal digits')
    if real_prime_number(a+2):
        print(a,'- 1 and ',a,'+ 1 are twin prime numbers')
    wex = 1
    for x in range(3,a+1,2):
        if real_prime_number(x):
            wex += 1
    print(f'{a} is a {wex}th prime number.')
else:
    print(a,'is a composite number')
    for x in range(2,a):
        if a % x == 0:
            print('Least prime factor of',a,'is',x)
            break