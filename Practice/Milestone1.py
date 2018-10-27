#Asking for user choice of X or O
def userChoice():
    global  user1;
    global user2;
    user1 = input('User 1, please choose X or O: ').upper();

    user2 = input('User 2, please choose X or O: ').upper();
    checkChoice();

#Checking the first choice
def checkChoice():
    if user1 == user2:
        print('Invalid inputs, both the user cannot have the same value');
        userChoice();
    elif user1 not in ['X', 'O']:
        print('Invalid choice by User 1');
        userChoice();
    elif user2 not in ['X', 'O']:
        print('Invalid choice by User 2');
        userChoice();
    else:
        print('Let us Play');
        userInputNumber();

#printing the board
def printInitBoard():
    print('  |   |    ');
    print(cellNumbers[6] + ' | ' + cellNumbers[7] + ' | ' +cellNumbers[8]);
    print('----------');
    print((cellNumbers[3] + ' | ' + cellNumbers[4] + ' | ' +cellNumbers[5]));
    print('----------');
    print((cellNumbers[0] + ' | ' + cellNumbers[1] + ' | ' +cellNumbers[2]));
    print('  |   |    ');

#Assigning values into the list
def printBoard(usernum, userChoice):
    if userChoice == 'X' or userChoice == 'x':
        cellNumbers[usernum-1] = 'X';
        printInitBoard();
        return checkBoard(userChoice);

    elif userChoice == 'O' or userChoice =='o':
        cellNumbers[usernum - 1] = 'O';
        printInitBoard();
        return checkBoard(userChoice);

#Checking the win condition
def checkBoard(userChoice):
    if userChoice == cellNumbers[0] == cellNumbers[1] == cellNumbers[2] or userChoice == cellNumbers[3] == cellNumbers[4] == cellNumbers[5] \
            or userChoice == cellNumbers[6] == cellNumbers[7] == cellNumbers[8] or userChoice == cellNumbers[0] == cellNumbers[3] == cellNumbers[6] \
            or userChoice == cellNumbers[1] == cellNumbers[4] == cellNumbers[7] or userChoice == cellNumbers[2] == cellNumbers[5] == cellNumbers[8] \
        or userChoice == cellNumbers[0] == cellNumbers[4] == cellNumbers[8] or userChoice == cellNumbers[2] == cellNumbers[4] == cellNumbers[6] :
        print(userChoice + ' wins the game!!!!');
        return True;
    else:
        print('please continue playing!');
        return False;


#Checking the input
def checkNumber(userNum):
    if userNum not in range(1,10):
        print('Invalid input, please retry');
        return False;
    else:
        return True;

#Asking for input
def userInputNumber():
    global cellNumbers;
    cellNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
    printInitBoard();
    for i in range(0, 9):
        user1num = int(input('User1, please enter your number 1-9: '));
        if checkNumber(user1num):
            flag = printBoard(user1num, user1);
            if flag == True:
                break;
        user2num = int(input('User2, please enter your number 1-9: '));
        if checkNumber(user2num):
            flag2 = printBoard(user2num, user2);
            if flag2 == True:
                break;



#Let the game begin
userChoice();