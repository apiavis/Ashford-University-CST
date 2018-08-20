## Author: Alicia Piavis
## Title: Week 4 Interactive Assignment: Sorting a List and Using List Methods
## Course: CPT 200 Fundamentals of Programming Languages
## Instructor: Amjad Alkilani
## Date: 7/26/2018

## takes 20 numbers from the user as input
user_input = input('Please enter 20 integers separated by spaces only: ')

## splits numbers from user into separate strings
tokens = user_input.split()

## creates an empty list and then converts the data type to integer as each element is added to the list
user_nums = []
for token in tokens:
    user_nums.append(int(token))

print()

## sorts the list user_nums from least to greatest
user_nums.sort()

## pulls the lowest value from index 0, the highest value from the last index, and calculates the sum of the list
lowest_num = user_nums[0]
highest_num = user_nums[(len(user_nums)) - 1]
sum_nums = sum(user_nums)

## prints the output for lowest number, highest number, and sum
print('The lowest number in the list is: %d' % lowest_num)
print('The highest number in the list is: %d' % highest_num)
print('The sum of the numbers in the list is: %d' % sum_nums)

