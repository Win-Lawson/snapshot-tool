import os
import difflib
import filecmp
import re
import subprocess
import sys
import datetime as dt


def delta_num_words(initial, final):

    final_count = len(re.split('\W+', open(final).read()))
    initial_count = len(re.split('\W+', open(initial).read()))
    return final_count - initial_count


def detect_lua_err(file_path):
    return 0 != subprocess.run('luac -p ' + '"' + file_path + '"', shell=True, capture_output=True).returncode


def difference(initial, final, j):
    old_lines = open(initial).read().split('\n')
    new_lines = open(final).read().split('\n')
    a = difflib.HtmlDiff()
    result = '<title>'+str(j)+'</title>\n'
    result = result + a.make_file(fromlines=old_lines, tolines=new_lines, context=False)
    num_changed = delta_num_words(initial, final)
    err_prev = detect_lua_err(initial)
    err_curr = detect_lua_err(final)
    result = result + open("HTML/Additional Info.html").read().format(num_changed=num_changed, err_prev=err_prev,
                                                                      err_curr=err_curr, old=initial, new=final)
    return result



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
                file.write(difference(old, new, j+1))
                j = j+1
        if len(os.listdir(specific_diff_path)) == 0:
            os.rmdir(specific_diff_path)
