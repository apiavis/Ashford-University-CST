## Author: Alicia Piavis
## Title: Employee Management System Functionality 2
## Course: CPT 200 Fundamentals of Programming Languages
## Instructor: Amjad Alkilani
## Date: 7/15/2018


employee1 = [] ##creates an empty list for the data for employee 1

## takes user input for employee 1 data
employee1_name = input('Please enter the first and last name of employee 1: ')
employee1_ssn = input('Please enter the social security number of employee 1 with no spaces or dashes: ')
employee1_phone = input('Please enter the phone number of employee 1 with parentheses around the area code: ')
employee1_address = input('Please enter the email address of employee 1: ')
employee1_salary = input('Please enter the salary of employee 1 as an integer with no punctuation: ')
employee1_salary_new = '$' + employee1_salary ## adds a dollar sign onto the value for the employee1_salary

## adds elements to the empty list for employee 1
employee1.append(employee1_name)
employee1.append(employee1_ssn)
employee1.append(employee1_phone)
employee1.append(employee1_address)
employee1.append(employee1_salary_new)

print()
    
employee2 = [] ##creates an empty list for the data for employee 2

## takes user input for employee 2 data
employee2_name = input('Please enter the first and last name of employee 2: ')
employee2_ssn = input('Please enter the social security number of employee 2 with no spaces or dashes: ')
employee2_phone = input('Please enter the phone number of employee 2 with parentheses around the area code: ')
employee2_address = input('Please enter the email address of employee 2: ')
employee2_salary = input('Please enter the salary of employee 2 as an integer with no punctuation: ')
employee2_salary_new = '$' + employee2_salary ## adds a dollar sign onto the value for the employee2_salary

## adds elements to the empty list for employee 2
employee2.append(employee2_name)
employee2.append(employee2_ssn)
employee2.append(employee2_phone)
employee2.append(employee2_address)
employee2.append(employee2_salary_new)

print()

employee3 = [] ##creates an empty list for the data for employee 3

## takes user input for employee 3 data
employee3_name = input('Please enter the first and last name of employee 3: ')
employee3_ssn = input('Please enter the social security number of employee 3 with no spaces or dashes: ')
employee3_phone = input('Please enter the phone number of employee 3 with parentheses around the area code: ')
employee3_address = input('Please enter the email address of employee 3: ')
employee3_salary = input('Please enter the salary of employee 3 as an integer with no punctuation: ')
employee3_salary_new = '$' + employee3_salary ## adds a dollar sign onto the value for the employee3_salary

## adds elements to the empty list for employee 3
employee3.append(employee3_name)
employee3.append(employee3_ssn)
employee3.append(employee3_phone)
employee3.append(employee3_address)
employee3.append(employee3_salary_new)

print()

employee4 = [] ##creates an empty list for the data for employee 4

## takes user input for employee 4 data
employee4_name = input('Please enter the first and last name of employee 4: ')
employee4_ssn = input('Please enter the social security number of employee 4 with no spaces or dashes: ')
employee4_phone = input('Please enter the phone number of employee 4 with parentheses around the area code: ')
employee4_address = input('Please enter the email address of employee 4: ')
employee4_salary = input('Please enter the salary of employee 4 as an integer with no punctuation: ')
employee4_salary_new = '$' + employee4_salary ## adds a dollar sign onto the value for the employee4_salary

## adds elements to the empty list for employee 4
employee4.append(employee4_name)
employee4.append(employee4_ssn)
employee4.append(employee4_phone)
employee4.append(employee4_address)
employee4.append(employee4_salary_new)

print()

employee5 = [] ##creates an empty list for the data for employee 5

## takes user input for employee 5 data
employee5_name = input('Please enter the first and last name of employee 5: ')
employee5_ssn = input('Please enter the social security number of employee 5 with no spaces or dashes: ')
employee5_phone = input('Please enter the phone number of employee 5 with parentheses around the area code: ')
employee5_address = input('Please enter the email address of employee 5: ')
employee5_salary = input('Please enter the salary of employee 5 as an integer with no punctuation: ')
employee5_salary_new = '$' + employee5_salary ## adds a dollar sign onto the value for the employee5_salary

## adds elements to the empty list for employee 5
employee5.append(employee5_name)
employee5.append(employee5_ssn)
employee5.append(employee5_phone)
employee5.append(employee5_address)
employee5.append(employee5_salary_new)

print()

## creates empty list for all 5 employees
employee = [employee1, employee2, employee3, employee4, employee5]

## requests input from the user for which employee they would like to reference
employee_requested = int(input('Please enter the employee number that you would like to request information for (1-5): '))
index_number = employee_requested - 1 ## converts the employee number into the correct index position number

print()

## prints the employee information
print('The information for employee', employee_requested, 'is: \n')
print(','.join(employee[index_number])) ##removes the list syntax, and adds a comma in between each list element



