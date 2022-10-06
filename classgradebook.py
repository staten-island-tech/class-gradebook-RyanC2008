grade_list = []
student = 'Ryan Chen'

def get_average(grades_list):
    return sum(grades_list) / len(grades_list)

while True:
    grade = input('Please input grades or enter Q to quit: ')
    if grade == 'Q':
        break
    else: 
        grade_list.append(int(grade))
    
grade_avg = get_average(grade_list)

dictionary = {'Name': student, 'Class': '26B', 'Grades' : grade_list}
print (dictionary)
print (f'Your grade average for Ryan Chen is {grade_avg}' )