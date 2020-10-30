text = input('Enter your text: ')
keyCount = input('Enter the number of keys: ')
keyCount = int(keyCount)
output = ''
first = True
mode = input('encrypt or decrypt: ')

for n in range(keyCount):
    key = input('Enter thou key: ')
    key = int(key)
    #key = 13
    #do NOT change in case you dont know what you are doing these are the encryptable characters
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #translated = ''
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
                print('\nEncrypted text be like: ' + output + '\n')

            else:
                print('\nDecrypted text be like: ' + output + '\n') 
