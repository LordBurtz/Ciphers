from array import *

def main():
    text = input('The text that should be bruteforced: ')
    output = bruteforce(text)
    print(output)

def bruteforce(input):
    input = input.upper()
    output = []
    keys = []
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(characters)):
        result = ''

        for symbol in input:
            if symbol in characters:
                num = characters.find(symbol)
                num = num - key

                if num < 0:
                    num = num + len(characters)
                result = result + characters[num]
            else:
                result = result + symbol
        #print('Key #%s: %s' % (key, result)) //for printing result + key
        key = int(key)
        output.insert(key,result)
        keys.insert(key, key)

    return output



if __name__ == '__main__':
    main()
