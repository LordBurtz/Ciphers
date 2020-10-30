#by Fingolfin#5731
import sys
def main():
    print('\nEncrypt/Decrypt with a CaesarCipher')
    text = input('Enter your text: ')
    mode = input('encrypt or decrypt: ')
    if mode != 'encrypt' or 'decrypt':
        print('Error: wrong mode entered')
        sys.exit(0)

    count = input ('keycount: ')

    print('Output: ' + encrypt(text, count, mode))


def encrypt(text, keyCount, mode):
    keyCount = int(keyCount)
    output = ''
    first = True
    count = 0

    if mode != 'encrypt' or 'decrypt':
        print('Error: wrong mode entered')
        sys.exit(0)

    for n in range(keyCount):
        key = input('Enter the key: ')
        key = int(key)

        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if first == True:
            work = text
        else:
            work = ''.join(output)
            output = ''

        work = work.upper()
        for symbol in work:
            if symbol in LETTERS:
                number = LETTERS.find(symbol)
                if mode == 'encrypt':
                    number = number + key
                elif mode == 'decrypt':
                    number = number - key
                if number >= len(LETTERS):
                    number = number - len(LETTERS)
                elif number < 0:
                    number = number + len(LETTERS)

                output = output + LETTERS[number]
                first = False

            else:
                output = output + symbol
                first = False


            if range(len(text)) == range(len(output)):
                count += 1
                if count == keyCount:
                    return output




if __name__ == '__main__':
    main()
