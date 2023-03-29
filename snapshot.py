"""
STEM+C Snapshot Tool V2. This tool take snapshots of student code on the active server and stores
iterations locally on a user specified directory. This script is designed to run continuously, but
rerunning will not overwrite past files.
"""
import os
import shutil
import datetime as dt
import filecmp

import threading as th
import time


def get_source_path():
    """

    :return: returns path to /computer directory on active server
    """
    print('List of suggested source paths:')
    suggested_paths = []
    for path, dir_names, filenames in os.walk(os.getcwd()):
        if path.endswith('computer'):
            suggested_paths.append(path)
    for x, path in enumerate(suggested_paths):
        print(str(x)+': ', path)
    path_num = int(input("Input number of desired path: "))
    return suggested_paths[path_num]


def get_destination_path():
    """

    :return: returns path to save location for snapshots
    """
    result = 'CC Snapshots'
    user_destination = input("Enter destination path or leave blank to use '/CC Snapshots'\n")
    if not len(user_destination) == 0:
        result = user_destination
    return os.path.join(os.getcwd(), result)


def newest(path):
    """

    :param path: path to a directory
    :return: returns the newest file in supplied directory if one or more files exists
    """
    files = os.listdir(path)
    if len(files) != 0:
        paths = [path + '/' + basename for basename in files]
        return max(paths, key=os.path.getctime)
    return ""


def tstamp_copy(src_path, dest_path, filename):
    """Creates a snapshot of a single file, using a new filename so that previous iterations are
    not overwritten

    :param src_path: path to file to copy
    :param dest_path: where to copy it to
    :param filename: just the filename of the file to copy
    """
    curr_latest = newest(dest_path)
    path_latest = os.path.join(dest_path, curr_latest)
    if not filecmp.cmp(path_latest, src_path):
        timestamp = str(dt.datetime.now())[6:-7]
        dest_path = os.path.join(dest_path, filename)
        dest_path = dest_path[:-4] + ' ' + timestamp + '.lua'
        shutil.copyfile(src_path, dest_path)


def take_snapshot(src_path, dest_path):
    """ Creates timestamped copies for files in source_path and recursively calls
    on itself for subdirectories of source_path. Copied files are organized into directories
    with names that match the source file. Appends at destination_path does not overwrite.
    :param src_path: path to take snapshot of
    :param dest_path: path to save snapshots to
    :return: None
    """
    files = []
    directories = []
    for entry in os.listdir(src_path):
        entry_path = os.path.join(src_path, entry)
        if os.path.isfile(entry_path):
            files.append(entry)
        else:
            directories.append(entry)
    for directory in directories:
        sub_src_path = os.path.join(src_path, directory)
        sub_dest_path = os.path.join(dest_path, directory)
        if not os.path.exists(sub_dest_path):
            os.mkdir(sub_dest_path)
        take_snapshot(sub_src_path, sub_dest_path)
    for file in files:
        file_src_path = os.path.join(src_path, file)  # absolute path to file to copy
        file_dest_path = os.path.join(dest_path, file)
        if '.lua' in file:
            if not os.path.exists(file_dest_path):
                os.mkdir(file_dest_path)
            tstamp_copy(file_src_path, file_dest_path, file)
        else:
            shutil.copyfile(file_src_path, file_dest_path)


def generate_name_index(dest_path):
    """After snapshots are taken using take_snapshot() this program searches for files with
    filenames including name where students were instructed to write their names. This generates
    an index associating the computer numbers with the names of the students

    :param dest_path: Path to snapshot directory
    """
    folders = []
    for file in os.listdir(dest_path):
        if os.path.isdir(os.path.join(dest_path, file)):
            folders.append(file)
    index = open(os.path.join(dest_path, 'Index of Names'), 'w')
    index_text = ''
    for folder in folders:
        for file in os.listdir(os.path.join(dest_path, folder)):
            if 'name' in file.lower() and 'lua' not in file:
                text_file = open(dest_path + '/' + folder + '/' + file, 'r')
                name = text_file.read()
                index_text = index_text + folder + ': ' + name + "\n"
                break
    index.write(index_text)
    index.close()


def key_capture_thread():
    """ Allows for the continuous taking of snapshots
    """
    global keep_going
    input()
    keep_going = False
    print('Taking last snapshot')


source_path = get_source_path()
destination_path = get_destination_path()
print('Source: ' + source_path)
print('Destination: ' + destination_path)
print('Beginning continuous snapshots, press [ENTER] to stop')

if not os.path.exists(destination_path):
    os.makedirs(destination_path)

keep_going = True
th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
while keep_going:
    take_snapshot(source_path, destination_path)
    print('Collected Snapshot')
    time.sleep(10)
generate_name_index(destination_path)
print('Done!')
