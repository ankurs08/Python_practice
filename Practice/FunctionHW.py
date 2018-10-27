def vol(radius):
    print((4/3) * 3.14 * (radius**3));

vol(2)

def ran_check(num, low, high):
    flag = 'false';
    for i in range(low, high+1):
        if i == num:
            flag = 'true';
            break;
        else:
            continue;
    if flag == 'true':
        print('yes the number is in range');
    else:
        print('Not in range')

ran_check(2, 3, 7)

def up_low(mystr):
    lowCount=0;
    upCount=0;
    for letter in mystr:
        if letter.islower():
            lowCount = lowCount +1;
        elif letter.isupper():
            upCount = upCount +1;

    print('Number of Lower letters is {f}' .format(f=lowCount));
    print('Number of Lower letters is {f}'.format(f=upCount));

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


def unique_list(mylist):
    x = []
    for num in mylist:
        if num not in x:
            x.append(num)

    print (x)


def multiply(myNums):
    product = 1;

    for i in range(0, len(myNums)):
        product = product * myNums[i]

    print(product)
multiply([1,2,3,-4])


def palindrome(mystr):
    myList = []
    flag = 'false'
    for letter in mystr:
        myList.append(letter)

    myRevList = myList[::-1];

    for i in range(0, len(myList)):
        if myList[i] == myRevList[i]:
            flag = 'true'
        else:
            flag = 'false'

    if flag == 'true':
        print('palindrome');
    else:
        print('NO!!!!!')


palindrome('abcbadef')


def ispangram(mystr):
    flag = 'false'
    alphaset = 'abcdefghijklmnopqrstuvwxyz';
    for letter in alphaset:
        if letter in mystr:
            flag = 'true';
        else:
            flag = 'false';

    if flag == 'true':
        print('the string is pangram')
    else:
        print('Not Pangram')

ispangram(" quik brown fox jumps over the lazy dog")