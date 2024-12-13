#Christopher Robles Serrano
#Module 11 Lab 1
#12/11/2024
#This program takes user input to write to a csv file. It takes in student names and grades.

import csv

#Function to grab first/last name.
def names(x):
    myName = input(f'What is the students {x} name?: ').capitalize()
    return myName
    

#Function to grab exam grades 1 at time passing in te name of the student.
def grades(x, name):
    #Using a boolean loop to validate exam grades as a float.
    while True:
        myGrade = input(f'What is the {name}\'s exam {x} grade?: ')
        try:
            myGrade = float(myGrade)
            return myGrade
        except ValueError:
            print('Not a valid numeral!')

#Open grades3.csv in write mode to submit all user data.
with open('grades3.csv', mode = 'w', newline = '' ) as myFile:
    #Creating header names
    headerNames = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

    #Creating a dictionary writer passing our file(myFile) and our header values(headerNames)
    writer = csv.DictWriter(myFile, fieldnames = headerNames)
    
    #Writing our header
    writer.writeheader()

    #Loop to keep submitting user data as long as the user wants to using myContinue as our value. 
    myContinue = 'y'
    while myContinue == 'y':
        #Calling name function to get the first and last name
        firstName = names('first')
        lastName = names('last')

        #Combining names
        fullName = f'{firstName} {lastName}'

        #Calling grades function passing in the exam number and full name to get the grade for the student's exam.
        examGrade1 = grades(1, fullName)
        examGrade2 = grades(2, fullName)
        examGrade3 = grades(3, fullName)

        #Writing user inputs to myFile(grades3.csv) using writer.writerow() passing in all user data.
        writer.writerow({'First Name' : firstName, 'Last Name' : lastName, 'Exam 1': examGrade1, 'Exam 2': examGrade2, 'Exam 3' : examGrade3})

        #Checking if the user wants to continue to add data.
        myContinue = input('Would you like to enter another student? (y or n): ').lower()
        while myContinue not in ['y','n']:
            print('Invalid option!')
            myContinue = input('Would you like to enter another student? (y or n): ').lower()

    print('Data transfer successful!')

#Opening grades3 file in read mode.
with open('grades3.csv', mode='r', newline='') as myFile:
    #Creating our reader.
    reader = csv.reader(myFile)
    
    #Skipping our header to read the user data rows.
    header = next(reader)
    print('Summary:\n')
    
    #For loop to read our rows line by line.
    for row in reader:

        #Assigning each collumn of each row to a value.
        fName, lName, exam1, exam2, exam3 = row

        #Converting the our exam grades from strings to floats.
        exam1 = float(exam1)
        exam2 = float(exam2)
        exam3 = float(exam3)

        #Finding the average
        average = (exam1 + exam2 + exam3)/3

        #Formatted print statement to the terminal.
        print(f'Student: {fName} {lName}\nExam grades:{exam1, exam2, exam3}\nAverage:{average:.2f}\n')