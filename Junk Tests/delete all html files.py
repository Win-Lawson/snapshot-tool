import os

print(os.listdir('../input files'))
for student in os.listdir('../input files'):
    for project in os.listdir('input files' + '/' + student):
        if '.txt' not in project:
            for file in os.listdir('input files' + '/' + student + '/' + project):
                if 'html' in file:
                    os.remove('input files' + '/' + student + '/' + project+'/'+file)