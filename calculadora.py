n1= 0
n2= 0
resultado= 0
operacao= ' '

while True :
    n1= int(input('Digite o primeiro número: '))
    operacao= input('Digite a operação: ')
    n2= int(input('Digite o segundo número:'))
    if operacao == '+':
        resultado= n1+n2
    elif operacao == '-':
        resultado= n1-n2 
    elif operacao == '*':
        resultado= n1*n2
    elif operacao == '/':
        resultado= n1/n2 
    else :
        resultado= 'operação inválida'
    print(str(n1) + ' ' + str(operacao) +  str(n2) + ' = ' + str(resultado))
