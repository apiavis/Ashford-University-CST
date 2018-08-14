## Author: Alicia Piavis
## Title: Employee Management System Functionality 3
## Course: CPT 200 Fundamentals of Programming Languages
## Instructor: Amjad Alkilani
## Date: 7/22/2018


print('WELCOME TO YOUR EMPLOYEE MANAGEMENT SYSTEM')

## sets run_again variable to 'yes' to initiate loop that asks the user which function they want to utilize in the sytem
run_again = 'yes'
## creates empty list to store all employees that are added
employees = []

## loop that allows the user to choose the functionality of the system that they would like to execute
while run_again == 'yes':

    user_choice = int(input('If you would like to add new employees to the system, please enter 1.  If you would like to view employee information, please enter 2.  If you would like to close the program, please enter 3: '))
    employee_num = 1

    ## branch that allows user to input new employee(s)
    if user_choice == 1:
        total_employees = int(input('Please enter the number of employees that you would like to add to the database: '))
        user_response = 'yes'
        while user_response == 'yes':

            ## takes user input for employee data
            for i in range(total_employees):
                employee = [] ##creates an empty list for the data for one employee
                print('Please enter the first and last name of employee %s : ' % employee_num)
                employee_name = input()
                print('Please enter the social security number of employee %s with no spaces or dashes: ' % employee_num)
                employee_ssn = input()
                print('Please enter the phone number of employee %s with parentheses around the area code: ' % employee_num)
                employee_phone = input()
                print('Please enter the email address of employee %s : ' % employee_num)
                employee_address = input()
                print('Please enter the salary of employee %s as an integer with no punctuation: ' % employee_num)
                employee_salary = input()
                employee_salary_new = '$' + employee_salary ## adds a dollar sign onto the value for the employee_salary

                ## adds elements to the empty list for employee 1
                employee.append(employee_name)
                employee.append(employee_ssn)
                employee.append(employee_phone)
                employee.append(employee_address)
                employee.append(employee_salary_new)

                ## adds employee information to the broader list 'employees' at a new index
                employees.append(employee)

                employee_num += 1

            else:

                print()
                user_response = input('Would you like to add more employees to the system (yes or no)?')
                print()

        ## asks the user if they want to do another activity inside the employee management system
        run_again = input('OK. Would you like to add another employee to the system or view employee information (yes or no)?')

    ## branch that allows user to acquire information about employees
    elif user_choice == 2:
        employee_count = len(employees)
        ## branch that allows user to choose whether they want info on all employees, or just one
        user_choice_2 = int(input('Enter 1 if you would like to view all employee information.  Enter 2 if you would like to choose a specific employee: '))
        while (user_choice_2 != 1) and (user_choice != 2):
            user_choice_2 = input('Please enter a valid response.  Enter 1 if you would like to view all employee information.  Enter 2 if you would like to choose a specific employee: ')
        ## prints information about all employees
        if user_choice_2 == 1:
            for information in employees:
                print(information, '|')
        else:
            employee_requested = int(input('Please enter the employee number that you would like to request information for (1- %d): ' % employee_count))
            index_number = employee_requested - 1 ## converts the employee number into the correct index position number

            print()

            ## prints the information about a specific employee
            print('The information for employee', employee_requested, 'is: \n')
            print(','.join(employees[index_number])) ##removes the list syntax, and adds a comma in between each list element

            run_again = input('OK. Would you like to add another employee to the system or view employee information (yes or no)?')

    ## branch that allows user to exit the loop and employee management system
    elif user_choice == 3:
        print('You are exiting the Employee Management System.')
        run_again = 'no'

print('Thank you.  Goodbye.')
