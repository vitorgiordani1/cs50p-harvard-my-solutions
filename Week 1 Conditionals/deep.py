def asnwer(word):
    if word == '42':
        print('yes')
    elif word == 'forty two':
        print('yes')
    elif word == 'Forty Two':
        print('yes')
    elif word == 'forty-two':
        print('yes')
    elif word == 'FoRty TwO':
        print('yes')
    else:
        print('no')

def main():
    ask = str(input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')).strip()
    asnwer(ask)

main()
