#Level1

def lesser_of_two_evens(a, b):
     if a % 2 == 0 and b % 2 == 0:
         if a > b:
             print('both numbers are even and lesser is' + str(b))
         else :
             print('both numbers are even and lesser is' + str(a))
     else:
         if a > b:
             print('both numbers are odd and' + str(a) + ' is greater')
         else :
             print('both numbers are odd and' + str(b) + ' is greater')
#could have used min and max functions


lesser_of_two_evens(10, 20)


def animal_crackers(str):
    mylist = str.split()
    word1 = mylist[0]
    word2 = mylist[1]

    letter1 = word1[0]
    letter2 = word2[0]

    print(letter1 == letter2)

animal_crackers('lying plama')

def makes_twenty(num1, num2):
    if num1 + num2 == 20:
        return True
    elif num1 == 20 or num2 == 20:
        return True
    else:
        return False

print(makes_twenty(2 , 1))


def old_macdonald(str):
    if len(str) >= 4:
        print(str[0:3].capitalize() +  str[3:].capitalize())
    else:
        print(str.capitalize())


old_macdonald('mac')

def yoda(str):
    mylist = str.split(' ')
    print(' '.join(mylist[::-1]))

yoda('i am late')
#This is a good example how slicing may work to reverse


def almost_there(num):
    return num >=90 and num <=110  or num >=190 and num <=210

print(almost_there(90))

#Level2

#range is a very important function to be used in for loop
def has_33(nums):
    for num in range(0,len(nums)-1):
        if nums[num] == 3 and nums[num+1] == 3:
            print('true')
        else:
            print('false')

has_33([1,3,3,4])


def paper_doll(str):
    str3 = ''
    for char in str:
        str3 += (char * 3)
    print(str3)

paper_doll('Ankur')

def blackjack(num1, num2, num3):
    sum = num1 + num2 + num3
    if num1 == 11 or num2 == 11 or num3 ==11:
        sum = sum - 10
    if sum <= 21 :
        print(sum)
    else:
        print('BUST!')

blackjack(9, 9, 11)

#concept of flag needs to be used here
def summer_69(arr):
    flag = 'false';
    sum = 0;
    for num in arr:
        if num == 6:
            flag = 'true';
        elif num == 9:
            flag = 'false'

        if flag == 'false':
            if num == 9:
                sum = sum + num -9;
            else:
                sum = sum + num;

    print('sum is {f}' .format(f=sum));


summer_69([2, 1, 6, 9, 11])




def spy_game(list):
    count0 = 0
    spyFlag='false';
    for num in list:
        if num == 0:
            count0= count0 + 1;

        if num == 7 and count0 ==2:
            spyFlag='true';

    if spyFlag =='true':
        print('spy number')
    else:
        print('NO!')



spy_game([1, 0,0,0,7,2,0,4,5,0])


map()