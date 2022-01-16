import os

print(os.listdir('../actual kids COPY'))
for student in os.listdir('../actual kids COPY'):
    for project in os.listdir('actual kids COPY' + '/' + student):
        if '.txt' not in project:
            for file in os.listdir('actual kids COPY' + '/' + student + '/' + project):
                if 'html' in file:
                    os.remove('actual kids COPY' + '/' + student + '/' + project+'/'+file)