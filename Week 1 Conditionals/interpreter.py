#essa a parte que calcula as coisas
def math(number1, expressor, number2):                                 #o codigo é uma mini calculadora
    if expressor == '+':
        operator1 = number1 + number2
        print(f'{operator1:.1f}')

    elif expressor == '-':
        operator2 = number1 - number2
        print(f'{operator2:.1f}')

    elif expressor == '*':
        operator3 = number1 * number2
        print(f'{operator3:.1f}')


    elif expressor == '/':
        operator4 = number1 / number2
        print(f'{operator4:.1f}')
    elif expressor == '**':
        operator5 = number1 ** number2
        print(f'{operator5:.1f}')


# aqui converte para inteiros
def convert(a):
    a = int(a)
    return a

#asnwer
#aqui é a função principal
def main():
    expression = input("type your math Expression/ q to quit: ")

    x, y, z = expression.split(" ")
    number1 = convert(x)
    number2 = convert(z)
    math(number1, y, number2)




main()
