'''
this program will replace vowels in entered phrase by letter 'g'
and displyes the phrase as translated phrase
'''

def translator(phrase):

    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
             translation = translation + "g"
        elif letter.isupper():
             translation = translation + "G"
        else:
             translation = translation + letter
    return translation


print(translator(input("enter a phrase: ")))


