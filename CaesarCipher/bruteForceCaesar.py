#brute force 'em

crack = input('Crack this: ')
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    output = ''

    for symbol in crack:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(LETTERS)

            output = output + LETTERS[num]

        else:
            output = output + symbol

    print('Key #%s: %s' % (key, output))
