def main():
    text = input('Scramble this text: ')
    key = input('the key: ')
    key = int(key)

    encrypted = encrypt(key, text)

    print(encrypted + '|')

def encrypt(key, text):
    encrypted = [''] * key
    for col in range(key):
        counter = col

        while counter < len(text):

            encrypted[col] += text[counter]
            counter += key

    return ''.join(encrypted)

if __name__ == '__main__':
    main()
