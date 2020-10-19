text = input('Enter here: ')
output = ''

i = len(text) - 1
while i >= 0:
    output = output + text[i]
    i = i -1

print(output)
