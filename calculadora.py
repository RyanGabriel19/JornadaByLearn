print("---------CALCULADORA---------")


n1 = float(input('Digite o primeiro número:  '))

operacao = str(input('Digite a operação (+ , - , * , / ) : '))

n2 = float(input('Digite o segundo número: '))

if operacao == '+':
    soma = n1 + n2
    print('{} + {} = {}'.format (n1, n2, soma))

if operacao == '-':
    sub = n1 - n2
    print("{} - {} = {}".format (n1, n2, sub))

if operacao == '*':
    mult = n1 * n2
    print("{} * {} = {}".format (n1, n2, mult))

if operacao == "/":
    div = n1 / n2
    print("{} / {} = {}".format (n1, n2, div))
