import os


def gen_index():
    index = open('index.html', 'w')

    result = '<title>Home</title>\n'
    result = result + open('HTML/index_structure.html').read()
    for student in os.listdir('actual kids COPY'):
        result = result + open('HTML/student_row.html').read().format(student_path='HTML_OUT/TESTIZER.html', student_name=student, num_syntax_error='0',
                                                                      num_err_free='0', num_files='0', num_projects='0')

    index.write(result)
    index.close()


gen_index()
