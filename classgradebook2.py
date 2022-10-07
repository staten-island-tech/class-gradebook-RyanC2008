student_list = []
grade_list = []


def find_average(grade_list):
    return sum(grade_list) / len(grade_list)



while True:
    student_name= input('Please input student name here: ')
    student_class= input(f'Please input {student_name}s class: ')
    student_list.append(student_name)
    break

while True: 
        grade = input(f'Please input grades for {student_name}s {student_class} class or enter Q to quit: ')
        if grade == 'Q':
            print('Thank you!')
            break
        else: 
            grade_list.append(int(grade))
        
        
while (1>0):
        continue_adding_students = input('Would you like to add another student?(Y/N): ') == 'Y'



grade_avg = find_average(grade_list)

student_dictionary = {'Name': student_name, 'Class': student_class, 'Grades': grade_list, 'Grade average': grade_avg}

print(student_dictionary)
