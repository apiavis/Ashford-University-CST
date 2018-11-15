## Author: Alicia Piavis
## Title: Employee Management System Functionality 4
## Course: CPT 200 Fundamentals of Programming Languages
## Instructor: Amjad Alkilani
## Date: 7/29/2018

## function that prints initial Menu Options for Employee Management System
def menu_options():
    print('Menu Options:\n'
'(1) Enter new employee(s) into the system.\n'
'(2) View all employees.\n'
'(3) Search information for one employee.\n'
'(4) Update information for an employee.\n'
'(5) Exit the Employee Management System.\n\n')

## function that allows new employees to be added to the system
def new_employees():
    print('\n')
    total_employees = int(input('Please enter the number of employees that you would like to add to the database: '))
    print('\n')
    employee_num = 1 ## used as a counter, depending on how many employees the user wants to add
    ## takes user input for new employee data
    for i in range(total_employees):
        employee = {} ##creates an empty dictionary for the data for one employee
        print('First and last name of employee %s : ' % employee_num, end='')
        employee_name = input()
        print('Social security number of employee %s with no spaces or dashes: ' % employee_num, end='')
        employee_ssn = input()
        print('Phone number of employee %s with parentheses around the area code: ' % employee_num, end='')
        employee_phone = input()
        print('Email address of employee %s : ' % employee_num, end='')
        employee_email = input()
        print('Salary of employee %s as an integer with no punctuation: ' % employee_num, end='')
        employee_salary = input()
        print('\n')
        print('---------------------------------------------------------------------')
        print('\n')
        employee_salary_new = '$' + employee_salary ## adds a dollar sign onto the value for the employee_salary

        ## adds new keys and values to the empty dictionary for each employee
        employee['Name'] = employee_name
        employee['SSN'] = employee_ssn
        employee['Phone'] = employee_phone
        employee['Email'] = employee_email
        employee['Salary'] = employee_salary_new

        ## adds 'employee' dictionary to the larger dictionary, 'employees'
        employees[employee_num] = employee

        employee_num += 1

    ## directs the user back to the main menu
    print('Thank you. You will now be directed back to the main menu.\n')
    print('\n')
    print('---------------------------------------------------------------------')
    print('\n')

## function that allows the user to view all employees
def view_all_employees():
    for name, name_info in employees.items():
        ## prints the employee name with data to follow
        print('----------------------------%s-----------------------------' % name_info['Name'])
        print('\n')

        ## iterates through the dictionary to get all employee information
        for key in name_info:
            print(key + ':', name_info[key])
        print('\n')
        print('---------------------------------------------------------------------')
        print('\n')
    ## directs the user back to the main menu
    print('Thank you. You will now be directed back to the main menu.\n')
    print('\n')
    print('---------------------------------------------------------------------')
    print('\n')

## function that allows the user to search for one employee
def search_for_employee():
        employee_requested = input('Social security number (only digits) of the employee that you would like to request information for: ')
        for name, name_info in employees.items():
            ## checks for presence of social security number in the dictionary
            if name_info['SSN'] == employee_requested:
                print('\n')
                ## prints the employee name with data to follow
                print('----------------------------%s-----------------------------' % name_info['Name'])
                print('\n')
                ## iterates through the dictionary to get all information for employee with the matching SSN
                for key in name_info:
                    print(key + ':', name_info[key])
                print('\n')
                print('---------------------------------------------------------------------')
                print('\n')
            ## error handling if SSN entered does not match employee in the system
            else:
                print('This employee does not exist in the system.')
                print('\n')
        ## directs the user back to the main menu
        print('Thank you. You will now be directed back to the main menu.\n')
        print('\n')
        print('---------------------------------------------------------------------')
        print('\n')

## function that prints options if a user would like to update information for an employee
def update_info_choice_menu_options():
    print('Update Employee Information Options:\n'
'(1) Update employee name.\n'
'(2) Update SSN.\n'
'(3) Update phone.\n'
'(4) Update email.\n'
'(5) Update salary.\n\n')

## function that allows the user to update information for one employee
def update_info():
    employee_requested = input('Social security number (only digits) of the employee that you would like to request information for: ' )
    for name, name_info in employees.items():
        ## checks for presence of social security number in the dictionary
        if name_info['SSN'] == employee_requested:
            print('\n')
            ## prints current info for employee as found in the system
            print('-----------------The current information for %s is: -----------------' % name_info['Name'])
            print('\n')
            ## iterates through the dictionary to get all information for employee with the matching SSN
            for key in name_info:
                print(key + ':', name_info[key])
            print('\n')
            print('---------------------------------------------------------------------')
            print('\n')
            update_info_choice_menu_options()
            ## takes user input to direct the following while loop and branch
            update_info_choice = int(input('Which option would you like (1-5)?: '))
            while (update_info_choice != 1) and (update_info_choice != 2) and (update_info_choice != 3) and (update_info_choice != 4) and (update_info_choice != 5):
                print('\n')
                print('Please enter a valid response.\n')
                update_info_choice_menu_options()
                update_info_choice = int(input('Which option would you like (1-5)?: '))
            ## branching statements that direct the user to update particular information for one employee
            if update_info_choice == 1:
                print('\n')
                name_info['Name'] = input('Please enter the new name for %s: ' % name_info['Name'])
                print('\n')
            elif update_info_choice == 2:
                print('\n')
                name_info['SSN'] = input('Please enter the new social security number (only digits) for %s: ' % name_info['Name'])
                print('\n')
            elif update_info_choice == 3:
                print('\n')
                name_info['Phone'] = input('Please enter the new phone (with parentheses around the area code) for %s: ' % name_info['Name'])
                print('\n')
            elif update_info_choice == 4:
                print('\n')
                name_info['Email'] = input('Please enter the new email for %s: ' % name_info['Name'])
                print('\n')
            elif update_info_choice == 5:
                print('\n')
                name_info['Salary'] = input('Please enter the new salary for %s: ' % name_info['Name'])
                print('\n')
            print('\n')
            ## prints current info for employee in system after updates were made
            print('-----------------The current information for %s is: -----------------' % name_info['Name'])
            print('\n')
            ## iterates through the dictionary to print all information for employee after updates
            for key in name_info:
                print(key + ':', name_info[key])
            print('\n')
            print('---------------------------------------------------------------------')
            print('\n')
    ## directs the user back to the main menu
    print('Thank you. You will now be directed back to the main menu.\n')
    print('\n')
    print('---------------------------------------------------------------------')
    print('\n')

## function that allows the user to exit the Employee Management System
def exit_system():
    print('You are exiting the Employee Management System.')
    run_again = 'no'
    return

## start of program
print('\n')
print('\n')
print('------------------------------------------')
print('WELCOME TO YOUR EMPLOYEE MANAGEMENT SYSTEM')
print('------------------------------------------')
print('\n')
## sets run_again variable to 'yes' to initiate the loop that asks the user which function they want to utilize in the sytem
run_again = 'yes'
## creates empty dictionary to store all employees that are added
employees = {}

## loop that allows the user to choose the functionality of the system that they would like to execute
while run_again == 'yes':

    menu_options()
    ## takes user input to direct the following while loop and branch
    user_choice = int(input('Which option would you like (1-5)?: '))
    print('\n')
    while (user_choice != 1) and (user_choice != 2) and (user_choice != 3) and (user_choice != 4) and (user_choice != 5):
        print('Please enter a valid response.\n')
        menu_options()
        user_choice = int(input('Which option would you like (1-5)?: '))
    ## branch that allows user to input new employee(s)
    if user_choice == 1:
        new_employees()
    ## branch that allows user to view all employees
    elif user_choice == 2:
        view_all_employees()
    ## branch that allows user to search for one employees
    elif user_choice == 3:
        search_for_employee()
    ## branch that allows user to udpate information for one employee
    elif user_choice == 4:
        update_info()
    ## branch that allows user to exit the loop and employee management system
    elif user_choice == 5:
        exit_system()
        run_again = 'no'

print('Thank you.  Goodbye.')
