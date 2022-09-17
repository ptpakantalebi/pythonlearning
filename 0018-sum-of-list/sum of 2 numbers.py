a = input('enter the numbers: ')
c = a.split(' ')
d = list(map(lambda e:int(e),c))
while True:
    b = input()
    if b == 'END':
        break
    for x in d:
        t = int(b)-x
        if x < int(b):
            if t in d:
                print(x,t)