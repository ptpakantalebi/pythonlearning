input_text = input('enter the text: ')
if input_text[0] == 'P':
    split_input = input_text.split(' ')
    for x in range(1,len(split_input)):
        print(x-1 , split_input[x])
else:
    list1 = []
    while True:
        words = input('enter the word: ')
        if words == 'END':
            break
        list1.append(words)

print(*list1,sep=' ')