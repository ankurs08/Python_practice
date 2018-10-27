a = 50
b = 20
c = 30

def compare():
    if a > b or b > c :
        print('a is greatest')
    else:
        print('random string')

compare()

def piglatin(word):
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        print(word+'ay')
    else:
        print(word[1:]+word[0]+'ay')

piglatin('ADop')


def myfunc(str):
    mylist = []
    for index, letter in enumerate(str):
        if index % 2 == 0:
            mylist.append(letter.lower())
        else:
            mylist.append(letter.upper())
    print(mylist)
    print(''.join(mylist))
    return ''.join(mylist)


myfunc('Anthromorphism')


