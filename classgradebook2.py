student_list = []
grade_list = []

def find_average(grade_list):
    return sum(grade_list) / len(grade_list)

while True:
    student_name = input('Please input student name here: ')
    grade = input(f'Please input grades for {student_name} or enter Q to stop: ')
    if grade == 'Q':
        break
    else: 
        grade_list.append(int(grade))


    
    
