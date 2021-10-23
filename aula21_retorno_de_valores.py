def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(2, 3, 5)
r2 = somar(3,1)
r3 = somar(8)

print(f'Os resultados foram {r1}, {r2} e {r3}')

def fatorial (num=1):
    f = 1
    for c in range(num, 0, -1):
        f *=c
        return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')
