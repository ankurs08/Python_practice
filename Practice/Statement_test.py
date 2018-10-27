# Question 1
st = 'Print only the words that start with s in this sentence'

# print out the words that starts with s
def que1():
    st2 = st.split()
    for word in st2:
        if word[0] == 's':
            print(word)
        else:
            continue


# Question2
# Use range() to print all the even numbers from 0 to 10
def que2():
    for num in range(0, 10):
        if num%2 == 0:
            print(num)
        else:
            continue


# Question 4
# Go through the string below and if the length of a word is even print "even!"
st4 = 'Print every word in this sentence that has an even number of letters'

def que4():
  #  st4split = st4.split()
    for word in st4.split():
        if len(word)%2 == 0:
            print (word)
        else:
            continue

# Question 5
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
def que5():
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print('FizzBuzz')
        elif num%3 == 0:
            print ('Fizz')
        elif num%5 == 0:
            print ('Buzz')
        else:
            print (num)

