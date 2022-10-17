student_list = []
grade_list = []


def find_average(grade_list):
    return sum(grade_list) / len(grade_list)


def student_dictionary():
    student_name = input('Please input student name here: ')
    student_class = input(f'Please enter {student_name}s class here: ')
    while True:
            grade = input(f'Please input grades or enter Q to quit: ')
            if grade == 'Q':
                break
            grade_list.append(int(grade))
            grade_avg = find_average(grade_list)
            student_dictionary == {'Name': student_name,
                                 'Class': student_class,
                                 'Grade list': grade_list,
                                 'Grade average': grade_avg
                                 }   

student_dictionary()

while True:        
        continue_adding_students = input('Would you like to add one more student?(Y/N): ')
        if continue_adding_students == 'N':
                    print('Thank you for using this gradebook. Your student dictionaries are being printed now.')
                    print(student_dictionary)
                    break
        elif continue_adding_students == 'Y': 
            student_dictionary()

            

