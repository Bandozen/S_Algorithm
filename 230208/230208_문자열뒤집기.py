def my_reverse(string):
    reversename = ''
    for i in string:
        reversename = i + reversename
    return reversename


s = 'abcdefg'
print(my_reverse(s))