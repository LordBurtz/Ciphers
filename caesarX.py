text = input('Enter your text: ')
keyCount = input('Enter the number of keys: ')
keyCount = int(keyCount)
translated = ''
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
        work = ''.join(translated)
        translated = ''

    work = work.upper()
    for symbol in work:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]
            first = False

        else:
            translated = translated + symbol
            first = False


        if range(len(text)) == range(len(translated)):
            if mode == 'encrypt':
                print('\nEncrypted text be like: ' + translated + '\n')

            else:
                print('\nDecrypted text be like: ' + translated + '\n')
