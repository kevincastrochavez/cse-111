def main():
    i_number = input('Enter your I-Number: ')
    student_dict = open_file('students.csv')
    student_name = student_dict[i_number]

    if i_number in student_dict.keys():
        print(student_name)
    else:
        print('No such student')

def open_file(filename):
    with open(filename, "rt") as text_file:
        students = {}
        
        next(text_file)
        for line in text_file:
            student_list = line.split(',')
            key = student_list[0]
            value = student_list[1]

            students[key] = value

        return students
main()