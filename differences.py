import datetime
import os
import difflib
import filecmp
import re
import subprocess
import csv
import sys
import datetime as dt


# Methods used by difference
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
    try:
        extension = new.index('.')
        new = new[-13:-extension]
    except ValueError:
        new = new[-13:]

    old = old[-17:-4]
    new = new[-17:-4]

    print(old)
    print(new)
    new_time = datetime.datetime.strptime(new, '%m-%d %H-%M-%S')
    old_time = datetime.datetime.strptime(old, '%m-%d %H-%M-%S')
    return (new_time - old_time).total_seconds()


# Given two files, returns result: html diff | returns data: dictionary for insertion into csv file
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


welcome_text = """
Differences Tool: Given snapshots of code generated from snapshot.py, this script will generate a csv file with
detailing differences between iterations. Additionally the script will create HTML Diff files between successive iterations.
Copyright 2022 Win Lawson, UIUC STEM+C

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

INSTRUCTIONS: Please add input files from snapshot.py to the directory in which this script is running. 
Run this script with $ python3 differences.py

"""
print(welcome_text)
input("Press Enter to continue...")
os.system('cls||clear')

while True:
    files_index = 0
    files = []
    print("List of directories:")
    for file in os.listdir():
        if os.path.isdir(file):
            files.append(file)
    for file in files:
        print(str(files_index) + ' ' + file)
        files_index += 1
    try:
        selected_index = int(input("\nType number of input directory: "))
        if not 0 <= selected_index <= files_index - 1:
            raise ValueError
        else:
            input_path = files[selected_index]
            print('\nYour selected input path is "' + input_path + '"')
            output_path = input_path + "-output"
            print('output files will be saved in: "' + output_path + '"')
            cont = input('Do you want to continue? [Y/n]\n')
            if not (cont == 'y' or cont == 'Y'):
                raise ValueError
            else:
                break
    except ValueError:
        print("\nERROR: Invalid input or cancellation occurred, try again.\n")

fields = ['student', 'project', 'iteration', 'error?', 'fixed error', 'char count', 'word count', 'words changed',
          'if count', 'for count',
          'time spent', 'file path']

if not os.path.exists(output_path):
    os.mkdir(output_path)
with open(output_path + '/data.csv', 'w+') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    diffs_path = output_path + '/diffs'
    students = []
    projects = []
    instances = []
    for file in os.listdir(input_path):
        if os.path.isdir(input_path + '/' + file):
            students.append(file)
    for student in students:
        projects = []
        instances = []
        for file in os.listdir(input_path + '/' + student):
            if os.path.isdir(input_path + '/' + student + '/' + file):
                projects.append(file)
        for project in projects:
            instances = []
            specific_diff_path = diffs_path + '/' + student + '/' + project
            for instance in sorted(os.listdir(input_path + '/' + student + '/' + project)):
                instances.append(instance)
            j = 0
            for i in range(len(instances) - 1):
                if not os.path.isdir(specific_diff_path):
                    os.makedirs(specific_diff_path)
                old = input_path + '/' + student + '/' + project + '/' + instances[i]
                new = input_path + '/' + student + '/' + project + '/' + instances[i + 1]
                if not filecmp.cmp(old, new):
                    file = open(specific_diff_path + '/' + str(j + 1) + '.html', 'w+')
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
            #if len(os.listdir(specific_diff_path)) == 0:
               # os.rmdir(specific_diff_path)

print("Completed!")
