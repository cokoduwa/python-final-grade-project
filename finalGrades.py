#finalGrades.py
#Christina Okoduwa
#Final Grades for students 
#This program calcuates the students final grades.
#It asks the user for the amount of homework assignments, quizzes, and exams for each student.
#Then takes the average from each section then calculates the final grade using Homework as 20%, Quizzes as 40%, and Exams as 40% to come up with the grade.
#It allows the user to put several students.
#Once the user is done they can select the quit option to stop the program. 

def main():
    print("This program will calculate students final grade")#describes what the program will do.
    print()
    print ("Final grade will be calculated as followed:\n \t Homework: 20%\n \t Quizzes:  40%\n \t Exams:    40%") #states how the grades are calcuated.
    print()
    print("Please choose one of the following options:") #gives the user a prompt to select the option. 

    while True:
        
        print("\t 1.Calculate the student's grade\n \t 2.Quit")  #The user either selects option 1 for calculation or option 2 to quit. 

        

        cal = int (input("Option:  "))

        if cal == 2:
            print ("Goodbye")
        

        if cal == 1:  #if option 1 is chosen then it will calculate the student's grades. 
            print()
            print ("Homework calculations")
            print()
            totalhomeworkgrade = 0   #initalizing accumulator for homework grades. 
            homeworkgiven = int ( input ("How many homework assignments were given: ")) #asking user to enter amount of homework assignments given.
            print()
            for homework in range (homeworkgiven): 
                print ("\t Enter Homework", homework + 1, "grade", end = '') #will list the amount of homework assignments given.
                homeworkgrade = int (input(':')) #where the homework grades will be entered for each assignment given.

                while homeworkgrade < 0 or homeworkgrade > 100: # the homework grade has to be between 0 and 100 or error will be given.
                    print("Error, please enter correct homework grade between 0 and 100")
                    homeworkgrade = int (input(':'))
                    
                totalhomeworkgrade += homeworkgrade #will add up all the homework grades that were entered. 
            average_homework = totalhomeworkgrade / homeworkgiven #will take the average of the total amount of homework assignments divided by the actual amount of assignments given.
            print()
            print ("Average homework grade : "'%.1f'%average_homework)
            print()


            print ("Quiz calculations")
            print()
            totalquizzesgrade = 0   #initalizing accumulator for quizzes grades. 
            quizzesgiven = int ( input ("How many quizzes were given: ")) #asking user to enter amount of quizzes were given.
            print()
            for quizzes in range (quizzesgiven): 
                print ("\t Enter Quiz", quizzes + 1, "grade", end = '') #will list the amount of quizzes given.
                quizzesgrade = int (input(':')) #where the quiz grades will be entered for each quiz given.

                while quizzesgrade < 0 or quizzesgrade > 100: # the quiz grade has to be between 0 and 100 or error will be given.
                    print("Error, please enter correct quiz grade between 0 and 100")
                    quizzesgrade = int (input(':'))
                    
                totalquizzesgrade += quizzesgrade #will add up all the quizzes grades that were entered. 

            average_quizzes = totalquizzesgrade / quizzesgiven #will take the average of the total amount of quizzes divided by the actual amount of quizzes given. 
            print()
            print ("Average quiz grade : "'%.1f'%average_quizzes)
            print()


            print ("Exam calculations")
            print()
            totalexamsgrade = 0   #initalizing accumulator for exams grades. 
            examsgiven = int ( input ("How many exams were given: ")) #asking user to enter amount of exams were given.
            print()
            for exams in range (examsgiven): 
                print ("\t Enter Exam", exams + 1, "grade", end = '') #will list the amount of exams given.
                examsgrade = int (input(':')) #where the exams grades will be entered for each exam given.

                while examsgrade < 0 or examsgrade > 100: # the exam grade has to be between 0 and 100 or error will be given.
                    print("Error, please enter correct exam grade between 0 and 100")
                    examsgrade = int (input(':'))
                    
                totalexamsgrade += examsgrade #will add up all the exams grades that were entered. 
            average_exams = totalexamsgrade / examsgiven #will take the average of the total amount of exams divided by the actual amount of exams given. 
            print()
            print ("Average exam grade : "'%.1f'%average_exams)
            print()

            
            #declaring weight of final grades
            homework_percentage = 0.2
            quiz_percentage = 0.4
            exam_percentage = 0.4
            

            #calculating final grades
            final_grade = (average_homework * homework_percentage) + (average_quizzes * quiz_percentage) + (average_exams * exam_percentage)
            print ("Final grade of student is : "'%.1f'%final_grade)
            print()
            print ("Do you want to calculate another student grade? Choose from the options below ")
            print()
        else:
            break # breaks out of the loop
main() #calls function
                            
                   

    

    
