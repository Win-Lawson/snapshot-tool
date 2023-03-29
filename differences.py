import os
import glob
import csv
import re
import subprocess
import datetime as dt


def get_source_path():
    """

    :return: returns path to snapshots directory collected from snapshot tool
    """
    print('Select snapshot output folder:')
    suggested_paths = os.listdir()
    for x, path in enumerate(suggested_paths):
        print(str(x) + ': ', path)
    path_num = int(input("Input number of desired path: "))
    return suggested_paths[path_num]


def get_destination_path(src_path):
    """

    :param src_path: source path from get_source_path()
    :return: returns path to output location for difference tool
    """
    result = src_path + ' - diffs'
    user_destination = input("Enter destination path or leave blank to use '" + result + "'\n")
    if not len(user_destination) == 0:
        result = user_destination
    return os.path.join(os.getcwd(), result)


def walk_to_level(path, depth=1):
    """It works just like os.walk, but you can pass it a level parameter
       that indicates how deep the recursion will go.
       If depth is 1, the current directory is listed.
       If depth is 0, nothing is returned.
       If depth is -1 (or less than 0), the full depth is walked.
    """
    # If depth is negative, just walk
    # Not using yield from for python2 compat
    # and copy dirs to keep consistent behavior for depth = -1 and depth = inf
    if depth < 0:
        for root, dirs, files in os.walk(path):
            yield root, dirs[:], files
        return
    elif depth == 0:
        return

    # path.count(os.path.sep) is safe because
    # - On Windows "\\" is never allowed in the name of a file or directory
    # - On UNIX "/" is never allowed in the name of a file or directory
    # - On MacOS a literal "/" is quietly translated to a ":" so it is still
    #   safe to count "/".
    base_depth = path.rstrip(os.path.sep).count(os.path.sep)
    for root, dirs, files in os.walk(path):
        yield root, dirs[:], files
        cur_depth = root.count(os.path.sep)
        if base_depth + depth <= cur_depth:
            del dirs[:]


def get_files_by_date(path):
    files = glob.glob(os.path.join(path, '*'))
    files.sort(key=os.path.getmtime)
    return files


def get_word_count(path):
    return len(re.split('\W+', open(path).read()))


def get_char_count(path):
    string = open(path).read()
    return len(string) - string.count(' ')


def do_err_exist(file_path):
    try:
        subprocess.check_output('luac -p ' + '"' + file_path + '"', stderr=subprocess.STDOUT, shell=True)
    except Exception:
        return True
    return False


def count_key(file_path, key):
    file = open(file_path).read()
    return file.count(key)


def analyze(instances):
    for x in range(len(instances)):
        instance = instances[x]
        computer_id = instance.split('/')[1]
        project_name = instance.split('/')[2]
        iteration = x + 1
        error_exist = do_err_exist(instance)
        char_count = get_char_count(instance)
        word_count = get_word_count(instance)
        if_count = count_key(instance, 'if')
        for_count = count_key(instance, 'for')
        file_path = instance
        delta_word_count = 'NA'
        delta_char_count = 'NA'
        fixed_error = 'NA'
        time_spent = 'NA'
        if x > 0:
            previous_inst = instances[x - 1]
            delta_word_count = word_count - get_word_count(previous_inst)
            delta_char_count = char_count - get_char_count(previous_inst)
            if do_err_exist(previous_inst):
                fixed_error = not do_err_exist(instance)
            curr_time = dt.datetime.fromtimestamp(os.path.getmtime(instance))
            prev_time = dt.datetime.fromtimestamp(os.path.getmtime(previous_inst))
            time_spent = curr_time - prev_time
        data = {'computer': computer_id, 'project': project_name, 'iteration': iteration, 'error?': error_exist,
                'fixed error': fixed_error, 'char count': char_count, 'delta char count': delta_char_count,
                'word count': word_count, 'delta word count': delta_word_count, 'if count': if_count,
                'for count': for_count, 'time spent': time_spent, 'file path': file_path}
        writer.writerow(data)


source_path = get_source_path()
destination_path = get_destination_path(source_path)


if not os.path.exists(destination_path):
    os.mkdir(destination_path)

project_paths = []
for root, dirs, files in walk_to_level(source_path, 2):
    if root.count('/') == 2:
        project_paths.append(root)


fields = ['computer', 'project', 'iteration', 'error?', 'fixed error', 'char count', 'delta char count', 'word count',
          'delta word count',
          'if count', 'for count',
          'time spent', 'file path']


with open(os.path.join(destination_path, 'data.csv'), 'w+') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for project in project_paths:
        ordered_instances = get_files_by_date(project)
        analyze(ordered_instances)
