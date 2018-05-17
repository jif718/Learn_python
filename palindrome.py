forbidden_word = (' ',',','.','!','/','?','_',';',':')

def remove_dot(string):
    text_array = []
    for i in string:
        text_array.append(i)
    #print(text_array)

    text_array_temp = text_array[:]
    for i in text_array_temp:
        if i in forbidden_word:
            #print('{0} is in forbidden word.'.format(j))
            text_array.remove(i)
            #print('After remove:{0}'.format(text_array))

    #print(text_array)
    return text_array

def reverse(text):
    #print(text[::-1])
    return text[::-1]

def determine(text):
    if text == reverse(text):
        print('Yes, it is palindrome.')
    else:
        print('No, it isn\'t palindrome.')

text_string = str.lower(input('Please input:'))
removed_array = remove_dot(text_string)
reversed_array = reverse(removed_array)
determine(reversed_array)
