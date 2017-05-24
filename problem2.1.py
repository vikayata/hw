
a = str(input('Enter the word:'))
a = a.lower() #избавляемся от чувствительности регистра, а то будет неверно работать

'''word = 'Wow'
print(word.endswith(word[0]))'''


def is_palindrome(word=''):
    if not word.endswith(word[0]):
        return False
    word2 = word[1:-1]
    if len(word) < 2 or is_palindrome(word2):
        return True

print('This is a palindrome') if is_palindrome(a) else print('This is not a palindrome')

