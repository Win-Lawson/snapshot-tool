import datetime
import os
import difflib
import filecmp
import re
import subprocess
import csv
import sys
import datetime as dt


def word_count(path):
    return len(re.split('\W+', open(path).read()))


def char_count(path):
    string = open(path).read()
    return len(string) - string.count(' ')


def delta_word_count(initial, final):
    return word_count(final) - word_count(initial)


def do_err_exist(file_path):
    try:
        subprocess.check_output('luac -p ' + '"' + file_path + '"', stderr=subprocess.STDOUT, shell=True)
    except Exception:
        return True
    return False


def count_key(file_path, key):
    file = open(file_path).read()
    return file.count(key)


def time_diff(old, new):
    old = old[-17:-4]
    new = new[-17:-4]
    new_time = datetime.datetime.strptime(new, '%m-%d %H-%M-%S')
    old_time = datetime.datetime.strptime(old, '%m-%d %H-%M-%S')
    return (new_time - old_time).total_seconds()


def difference(initial, final, j):
    old_lines = open(initial).read().split('\n')
    new_lines = open(final).read().split('\n')
    a = difflib.HtmlDiff()
    result = '<title>' + str(j + 1) + '</title>\n'
    result = result + a.make_file(fromlines=old_lines, tolines=new_lines, context=False)
    num_changed = delta_word_count(initial, final)
    err_prev = do_err_exist(initial)
    err_curr = do_err_exist(final)
    result = result + open("HTML/Additional Info.html").read().format(num_changed=num_changed, err_prev=err_prev,
                                                                      err_curr=err_curr, old=initial, new=final)
    data = {}
    data['error?'] = err_curr
    data['fixed error'] = err_prev and not err_curr
    data['words changed'] = num_changed
    data['time spent'] = time_diff(old, new)
    return result, data
    final_count = len(re.split('\W+', open(final).read()))
    initial_count = len(re.split('\W+', open(initial).read()))


fields = ['student', 'project', 'iteration', 'error?', 'fixed error', 'char count', 'word count', 'words changed',
          'if count', 'for count',
          'time spent', 'file path']
with open('output files/data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    path = 'input files'
    diffs_path = 'output files/diffs'
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
                    data['iteration'] = j + 2
                    data['char count'] = char_count(new)
                    data['word count'] = word_count(new)
                    data['if count'] = count_key(new, 'if ')
                    data['for count'] = count_key(new, 'for ')
                    data['file path'] = new
                    if j == 0:
                        temp = {}
                        temp['student'] = student
                        temp['project'] = project
                        temp['iteration'] = 1
                        temp['error?'] = do_err_exist(old)
                        temp['fixed error'] = 'N/A'
                        data['char count'] = char_count(old)
                        data['word count'] = word_count(old)
                        temp['words changed'] = 'N/A'
                        temp['if count'] = count_key(old, 'if ')
                        temp['for count'] = count_key(old, 'for ')
                        temp['file path'] = old
                        writer.writerow(temp)
                        data['iteration'] = 2
                        data['error?'] = do_err_exist(new)
                        data['file path'] = new
                    writer.writerow(data)
                    j = j + 1
            if len(os.listdir(specific_diff_path)) == 0:
                os.rmdir(specific_diff_path)
