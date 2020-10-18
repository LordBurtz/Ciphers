#SEVQBYVA, JVMHSPMR

import pyperclip

message =  input('Enter ur message: ')
key = input('Enter thou key: ')
key = int(key)

key2 = input('Enter thou key: ')
key2 = int(key2)

key3 = input('Enter thou key: ')
key3 = int(key3)
#key = 13
mode = input('encrypt or decrypt: ')
#do NOT change in case you dont know what you are doing these are the encryptable characters
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
translated2 = ''
translated3 = ''

message = message.upper()
for symbol in message:
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

    else:
        translated = translated + symbol

translated = translated.upper()
for symbol in translated:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key2
        elif mode == 'decrypt':
            num = num - key2
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated2 = translated2 + LETTERS[num]

    else:
        translated2 = translated2 + symbol

translated2 = translated2.upper()
for symbol in translated2:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key3
        elif mode == 'decrypt':
            num = num - key3
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated3 = translated3 + LETTERS[num]

    else:
        translated3 = translated3 + symbol


if mode == 'encrypt':
    print('\nEncrypted text be like: ' + translated3)

else:
    print('\nDecrypted text be like: ' + translated3)

#print('\nOutput: ' + translated)
#pyperclip.copy(translated) enable this if you are using windows and want
#it to be copied to your clipboard


#JVMHSPMR, COFALIFK
