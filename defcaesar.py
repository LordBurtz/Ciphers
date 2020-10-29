#by Fingolfin#5731
def main():
    print('Encrypt/Decrypt with a CaesarCipher')
    text = input('Enter your text: ')
    mode = input('encrypt or decrypt: ')
    count = input ('keycount: ')

    if mode == 'encrypt' or 'decrypt':
        print(encrypt(text, count, mode))
    else:
        print('Exception: wrong mode entered')



def encrypt(text, keyCount, mode):
    keyCount = int(keyCount)
    output = ''
    first = True
    count = 0

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
                if mode == 'encrypt':
                    count += 1
                    if count == keyCount:
                        return output

                else:
                    count += 1
                    if count == keyCount:
                        return output



if __name__ == '__main__':
    main()
