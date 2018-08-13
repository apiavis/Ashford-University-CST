## gets input from the user (integer greater than 1)
user_num = int(input('Enter an integer greater than 1: '))

## branching statements guided by the previous user input
if user_num <= 1:
    print('This program only accepts numbers greater than one.  Please start over.')
## determines which function will be executed next (depending on whether user enters 1 or 2)
else:
    user_choice = int(input('Please enter 1 or 2: '))
    if user_choice == 1:
        for i in range(user_num): ## prints countdown from user_num
            print(user_num)
            user_num += -1
        print('Goodbye.')
    if user_choice == 2:
        factorial = 1
        for i in range(user_num): ## calculates and prints factorial of user_num
            factorial = factorial * (i + 1)
        print(factorial)
        print('Goodbye.')
               
        
