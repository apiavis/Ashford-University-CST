## Author: Alicia Piavis
## Title: Week 5 Interactive Assignment: Program That Grades Driver's License Exam
## Course: CPT 200 Fundamentals of Programming Languages
## Instructor: Amjad Alkilani
## Date: 8/1/2018

answer_key = ['B', 'D', 'A', 'A', 'B', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']

# function that reads a text file and creates a list of the student's answer choices from the text file
def list_of_student_answers():
    print('Reading in data...')
    # opens the text file
    f = open('C:\\Users\\Alicia\\Documents\\CPT200_Wk5_InteractiveAssignment1_Student_Scorecard_.txt')
    # reads the information from the file
    student_answers = f.readlines()
    # closes the file
    f.close()

    # strips and slices each string element in the list to only contain the answer choice and then capitalizes it
    for index, answer in enumerate(student_answers):
        answer = answer.strip()
        answer = answer[-1:].upper()
        student_answers[index] = answer
    # returns list of student answers in a format matching that of the list answer_key
    return student_answers

# function that calculates the score (in number correct) that a student received
def grade_exam(student_responses):
    number_of_questions = len(answer_key) # calulates number of questions on the exam
    score = 0
    # iterates through each list to determine whether or not the student answer matches the answer key
    for i in range(number_of_questions):
        if answer_key[i] == student_responses[i]:
            score += 1
        else:
            score += 0
    return score

# function that creates a list of the question numbers that were answered incorrectly
def list_of_questions_marked_incorrect():
    number_of_questions = len(answer_key) # calulates number of questions on the exam
    incorrect_question_numbers = []
    # iterates through each list to determine identify the question numbers that were incorrect (using indices)
    for i in range(number_of_questions):
        if list_of_letters[i] != answer_key[i]:
            question_number = str(i + 1)
            incorrect_question_numbers.append(question_number) # adds the question number to a list
    return (', '.join(incorrect_question_numbers)) # returns the list as a single string without brackets


# Beginning of Program to Grade Student's Driver's License Exam
print('-----------------------------')
print("Driver's License Exam Grader")
print('-----------------------------\n')

# passes the returned value of list_of_student_answers outside of the function
list_of_letters = list_of_student_answers()
grade_exam(list_of_letters) # calls function grade_exam to generate a score from the list_of_letters
number_correct = grade_exam(list_of_letters) # calculates raw score
student_score = (number_correct / 20) * 100 # calculates score as a percentage
print("Student's Score: %d %% \n" % student_score)
number_incorrect = 20 - number_correct # calculates number incorrect
# branching statement that determines whether or not the student passed
if number_correct >= 15:
    print('Student has passed the exam.\n')
else:
    print('Student has not passed the exam.\n')
print('Number of questions correct: %d \n' % number_correct)
print('Number of questions incorrect: %d \n' % number_incorrect)
# calls the function to generate the list of question numbers that were marked incorrectly
list_of_questions_marked_incorrect()
# passes the returned value of list_of_questions_marked_incorrect outside of the function
incorrect_questions = list_of_questions_marked_incorrect()
print('Questions answered incorrectly are: %s \n' % incorrect_questions)
print('Please go back and review the exam.')
