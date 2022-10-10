student_list = []
grade_list = []

def find_average(grade_list):
    return sum(grade_list) / len(grade_list)

def create_new(dictionary):
    grade_avg = find_average(grade_list)
    student_dictionary = {'Name':student_name, 'Class':student_class, 'Grade list':grade_list, 'Grade average': grade_avg}
    return student_dictionary

while True:
    student_name = input('Please input student name here: ')
    student_class = input(f'Please enter {student_name}s class: ')
    print('Thank you!')
    break
    

while True:
    grade = input(f'Please input grades for {student_name}s {student_class} class or enter Q to quit: ')
    if grade == 'Q':
        grade_avg = find_average(grade_list)
        student_dictionary = {'Name':student_name, 'Class':student_class, 'Grade list':grade_list, 'Grade average':grade_avg}
        print(student_dictionary)
        break
    else: 
        grade_list.append(int(grade))

while True: 
    continue_adding_students= input('Would you like to create another student profile? (Y/N): ')
    if continue_adding_students == 'N':
        break
    if continue_adding_students == 'Y':
        while True: 
                student_name = input('Please input another students name here: ')
                student_class = input(f'Please enter {student_name}s class: ')
                print('Thank you!')
                grade = input(f'Please input grades for {student_name}s {student_class} class or enter Q to quit: ')
                if grade == 'Q':
                            student_dictionary = {'Name':student_name, 'Class':student_class, 'Grade list':grade_list, 'Grade average':grade_avg}
                            print(student_dictionary)
                            
                else: 
                    grade_list.append(int(grade))







