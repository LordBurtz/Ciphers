import pyperclip

message =  input('Enter ur message: ')
key = input('Enter thou key: ')
key = int(key)
#key = 13
mode = input('encrypt or decrypt: ')
#do NOT change in case you dont know what you are doing these are the encryptable characters
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''

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

if mode == 'encrypt':
    print('\nEncrypted text be like: ' + translated)

else:
    print('\nDecrypted text be like: ' + translated)

#print('\nOutput: ' + translated)
#pyperclip.copy(translated) enable this if you are using windows and want
#it to be copied to your clipboard
