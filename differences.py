import os
import difflib
import filecmp
import re
import subprocess
import csv
import sys
import datetime as dt


def delta_num_words(initial, final):

    final_count = len(re.split('\W+', open(final).read()))
    initial_count = len(re.split('\W+', open(initial).read()))
    return final_count - initial_count


def do_err_exist(file_path):
    try:
        subprocess.check_output('luac -p ' + '"' + file_path + '"', stderr=subprocess.STDOUT, shell=True)
    except Exception:
        return True
    return False


def difference(initial, final, j):
    old_lines = open(initial).read().split('\n')
    new_lines = open(final).read().split('\n')
    a = difflib.HtmlDiff()
    result = '<title>'+str(j+1)+'</title>\n'
    result = result + a.make_file(fromlines=old_lines, tolines=new_lines, context=False)
    num_changed = delta_num_words(initial, final)
    err_prev = do_err_exist(initial)
    err_curr = do_err_exist(final)
    result = result + open("HTML/Additional Info.html").read().format(num_changed=num_changed, err_prev=err_prev,
                                                                      err_curr=err_curr, old=initial, new=final)
    data = {}
    data['error?'] = err_curr
    data['fixed error'] = err_prev and not err_curr
    data['words changed'] = num_changed
    return result, data


fields = ['student', 'project', 'iteration', 'error?', 'fixed error', 'words changed', 'file path']
with open('data.cvs', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    path = 'actual kids COPY'
    diffs_path = 'diffs'
    students = []
    projects = []
    instances = []
    for file in os.listdir(path):
        if os.path.isdir(path + '/' + file):
            students.append(file)
    for student in students:
        projects = []
        instances = []
        for file in os.listdir(path + '/' + student):
            if os.path.isdir(path + '/' + student + '/' + file):
                projects.append(file)
        for project in projects:
            instances = []
            specific_diff_path = diffs_path + '/' + student + '/' + project
            for instance in sorted(os.listdir(path + '/' + student + '/' + project)):
                instances.append(instance)
            j = 0
            for i in range(len(instances) - 1):
                if not os.path.isdir(specific_diff_path):
                    os.makedirs(specific_diff_path)
                old = path + '/' + student + '/' + project + '/' + instances[i]
                new = path + '/' + student + '/' + project + '/' + instances[i + 1]
                if not filecmp.cmp(old, new):
                    file = open(specific_diff_path + '/' + str(j + 1) + '.html', 'w')
                    diff, data = difference(old, new, j)
                    file.write(diff)
                    data['student'] = student
                    data['project'] = project
                    data['iteration'] = j+2
                    data['file path'] = new
                    if j == 0:
                        temp = {'student': student, 'project': project, 'iteration': 1, 'error?': do_err_exist(old),
                                'fixed error': 'N/A', 'words changed': 'N/A', 'file path': old}
                        writer.writerow(temp)
                        data['iteration'] = 2
                        data['error?'] = do_err_exist(new)
                        data['file path'] = new
                    writer.writerow(data)
                    j = j+1
            if len(os.listdir(specific_diff_path)) == 0:
                os.rmdir(specific_diff_path)
