## Author: Alicia Piavis
## Title: Employee Management System Functionality 1
## Course: CPT 200 Fundamentals of Programming Languages
## Instructor: Amjad Alkilani
## Date: 7/7/2018

## prompts user to enter employee information for new employee
employeeName = input('Please enter your first and last name: ')
employeeSSN = input('Please enter your social security number with no spaces or dashes: ')
employeePhone = input('Please enter your phone number with parentheses around the area code: ')
employeeEmail = input('Please enter your email address: ')
employeeSalary = input('Please enter your salary as an integer with no punctuation: ')

## prints employee information to the screen
print('----------', employeeName, '----------')
print('SSN:', employeeSSN)
print('Phone:', employeePhone)
print('Email:', employeeEmail)
print('Salary: $', employeeSalary)
print('---------------------------------------')
