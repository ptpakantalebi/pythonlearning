import functools
print(functools.reduce(lambda a, b: a+b,range(int(input('enter the number: '))+1)))