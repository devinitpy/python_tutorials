
#function that gets the course data and returns the course raw grade
counter =0
def course_data():
    if counter == 0:
        name=raw_input("Name: ")
        course=raw_input("Course: ")
        course_unit=raw_input("course_unit1: ")
        counter=counter+1
    grade=raw_input("Course Grade: ")
    computed_grade(grade)
    


#function that gets the computed grade (logic)

def computed_grade(grade):
    print("Intial Grade value: {0}".format(grade))
    if grade=="A":
        grade=6
    elif grade=="B":
        grade=5
    elif grade=="C":
        grade=4
    elif grade=="D":
        grade=3
    elif grade=="E":
        grade=2
    elif grade=="O":
        grade=1
    elif grade=="F":
        grade=0
    else:
        course_data()

course_data()
        
#         n=course_data()
#         computed_grade(n)
#         #grades were enterd wrong lets terminate the progra
    #out putting computed Grade
#     print("Your grade is {0}".format(grade))
#     #determining performance
#     if grade >= 4:
#         print("good performance")
#     elif  grade >=2 and grade < 4:
#         print("average score")
#     else:
#         print("poor performance")

# def average(total,summation_subs):
#     avg=total/summation_subs
#     print("Average is :%f"%avg)


# total_grade = 0

# #entering in scores 3 times
# for i in range(0,2):
#     grade=course_data()
#     print("Grade in call {0}".format(i))
#     total_grade=grade+total_grade
#     print("Total Grade is currently {0}".format(total_grade))

# #getting average
# average(total_grade,3)
