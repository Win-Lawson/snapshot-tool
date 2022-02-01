import os
import glob

def gen_index():
    index = open('navigation/index.html', 'w')

    result = '<title>Home</title>\n'
    result = result + open('HTML/index_structure.html').read()
    for student in os.listdir('actual kids COPY'):
        student = student.split()[0]
        student_path = '/STEMC-snapshot-tool/navigation/students/' + student + '.html'
        result = result + open('HTML/student_row.html').read().format(student_path=student_path, student_name=student, num_syntax_error='0',
                                                                      num_err_free='0', num_files='0', num_projects='0')
        if not os.path.isdir('navigation/students/' + student):
            os.makedirs('navigation/students/' + student)
        gen_student(student)
    index.write(result)
    index.close()


def gen_student(student):
    test = open('navigation/students/' + student + '.html', 'w')
    result = '<title>' + student + '</title>\n'
    result = result + open('HTML/student_structure.html').read()
    projects = []
    path = '/home/nlawson3/PycharmProjects/STEMC-snapshot-tool/actual kids COPY/'
    print(glob.glob(path + student+'*')[0])
    for file in os.listdir(glob.glob(path + student+'*')[0]):
        if os.path.isdir(glob.glob(path + student+'*')[0]+'/'+file):
            projects.append(file)
    print(projects)
    for project in projects:
        if not os.path.isdir('navigation/students/' + student + '/' + project):
            os.makedirs('navigation/students/' + student + '/' + project)
    test.write(result)
    test.close()


gen_index()
