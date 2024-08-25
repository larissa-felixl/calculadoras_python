n1 = n2 =  0
op = None
while op != 0:
    print(' ')
    print('''---------- Calculadora python ----------
          Escolha sua operação:
          1- Adição
          2- Subtração
          3- Multiplicação
          4- Divisão
          5- Elevar ao quadrado
          0- Sair ''')
    op = int(input('Digite a operação desejada: '))
    if op == 0:
        print('Morreu Maria Prea!')
        break
    if op not in [1, 2, 3, 4, 5]:
        print('Deu erro, try to choose a new operation!')
        continue
    if op in [1, 2, 3, 4, 5]:
        n1 = int(input('Digite o primeiro número da operação: '))
        n2 = int(input('Digite o segundo número da operação: '))
        if op == 1:
                print(f'---------- {n1} + {n2} = {n1+n2} ----------')
        elif op == 2:
                print(f'---------- {n1} - {n2} = {n1-n2} ----------')
        elif op == 3:
                print(f'---------- {n1} x {n2} = {n1*n2} ----------')
        elif op == 4:
                print(f'---------- {n1} / {n2} = {n1/n2} ----------')
        elif op == 5:
            n3 = (input('Você vai querer elevar ao quadrado o primeiro número ou o segundo?[N1/N2] ')).upper().strip()
            if n3 == 'N1':
                    print(f'----------{n1} ^ 2 = {n1**2}----------')
            elif n3 == 'N2':
                    print(f'----------{n2} ^ 2 = {n2**2}----------')