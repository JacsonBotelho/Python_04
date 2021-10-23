n1=int(input('Digite um numero: '))
print('o numero digitado é {} \nSeu sucessor é {} \nO seu antecessor é {} '. format(n1,(n1-1),(n1+1)))

n=int(input('Digite um numero: '))
a=n-1
s=n+1
print('o numero digitado é {} \nSeu sucessor é {} \nO seu antecessor é {} '. format(n,a,s))


n=int(input('Digite um numero: '))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de {} vale {}.'.format(n,d))
print('O Triplo de {} é {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n,t,n,r))

n=int(input('Digite um numero: '))
print('O dobro de {} vale {}.'.format(n,(n*2)))
print('O Triplo de {} é {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n,(n*3),n,n**(1/2)))

n=int(input('Digite um numero: '))
print('O dobro de {} vale {}.'.format(n,n*2))
print('O Triplo de {} é {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n,n*3,n,pow(n,(1/2))))



n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
n3=int(input('Digite o terceiro numero: '))
n4=int(input('Digite o quarto numero: '))
n5=int(input('Digite o quinto numero: '))
s=n1+n2+n3+n4+n5
print('A soma dos numeros digitados é: {}'.format(s))