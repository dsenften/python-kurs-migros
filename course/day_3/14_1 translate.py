def sprache(text,
             vokale={'a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü'},
             diphtonge={'ei', 'au', 'ie', 'eu'},
             fueller='lef'):
    text = text.lower();
    kodiert = ''

    while text:
        first2 = text[:2] # ein oder zwei Zeichen
        first = text[0]

        if first in diphtonge:
            kodiert += first2 + fueller + first2
            text = text[2:]
        elif first in vokale:
            kodiert  += first + fueller + first
            text = text[1:]
        else:
            kodiert += first
            text = text[1:]

    return kodiert

words = ['Löffelsprache', 'Donauen', 'zweieiig', 'Treueeid']

for word in words:
    print(sprache(word))

print('\nUnd nun mit anderer Füllsilbe:')
for word in words:
    print(sprache(word, fueller='lol'))
