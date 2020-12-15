def is_palindrome(wort):
    wort = wort.lower()
    return wort == wort[::-1]


print(is_palindrome('Anna'))

word_list = eval(input('Bitte gib eine Wortliste ein: '))

for word in word_list:
    print(f'{word}: {is_palindrome(word)}')
