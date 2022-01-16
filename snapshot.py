import os
from ftplib import FTP
import datetime as dt
import filecmp
import time
import threading as th


def newest(path):
    files = os.listdir(path)
    paths = [path + '/' + basename for basename in files]
    return max(paths, key=os.path.getctime)


def copy_file(file, target_dir):
    time_stamp = str(dt.datetime.now())[6:-7]
    time_stamp = time_stamp.replace(':', '-')

    filename = file.split('.')[0]
    extension = ''
    if len(file.split('.')) > 1:
        extension = file.split('.')[1]

    folder = target_dir + '/' + file
    path = folder + '/' + filename + ' ' + time_stamp + '.' + extension

    if 'name' in file and 'lua' not in file:
        if not os.path.exists(target_dir + '/' + file):
            local_file = open(target_dir + '/' + file, 'wb')
            ftp.retrbinary('RETR ' + file, local_file.write, 1024)
            local_file.close()
        else:
            local_file = open(target_dir + '/' + file, 'wb')
            ftp.retrbinary('RETR ' + file, local_file.write, 1024)
            local_file.close()
    else:
        if not os.path.exists(folder):
            os.mkdir(folder)
            local_file = open(path, 'wb')
            ftp.retrbinary('RETR ' + file, local_file.write, 1024)
            local_file.close()
        else:
            latest = newest(folder)
            local_file = open(path, 'wb')
            ftp.retrbinary('RETR ' + file, local_file.write, 1024)
            local_file.close()
            if filecmp.cmp(path, latest):
                os.remove(path)
            else:
                print(file + ' was updated.')


def get_folder_list():
    def parse(line):
        if line[0] == 'd':
            result = ((line.rpartition(':')[2])[3:])
            folder_list.append(result)

    folder_list = []
    ftp.dir(parse)
    return folder_list


def get_file_list():
    def parse(line):
        if line[0] != 'd':
            result = ((line.rpartition(':')[2])[3:])
            file_list.append(result)

    file_list = []
    ftp.dir(parse)
    return file_list


def copy_dir(dir_from, dir_to):
    ftp.cwd(dir_from)
    files = get_file_list()
    for file in files:
        copy_file(file, dir_to)
    folders = get_folder_list()
    for folder in folders:
        if not os.path.exists(target + '/' + folder):
            os.mkdir(target + '/' + folder)
            sub_dir = dir_from + '/' + folder
            ftp.cwd(sub_dir)
            copy_dir(sub_dir, dir_to + '/' + folder)
        else:
            sub_dir = dir_from + '/' + folder
            ftp.cwd(sub_dir)
            copy_dir(sub_dir, dir_to + '/' + folder)


def generate_index_of_names():
    path = '../../Desktop/Snapshot tool/CC Snapshots'
    dirs = []
    for file in os.listdir(path):
        if os.path.isdir(path + '/' + file):
            dirs.append(file)
    index = open('../../Desktop/Snapshot tool/CC Snapshots/index of names.txt', 'w')
    index_text = ''
    for dir in dirs:
        for file in os.listdir(path + '/' + dir):
            if 'name' in file and 'lua' not in file:
                text_file = open(path + '/' + dir + '/' + file, 'r')
                name = text_file.read()
                index_text = index_text + dir + ': ' + name + "\n"
                break
    index.write(index_text)
    index.close()


# On Run

# Connect to FTP
ftp = FTP(host='69.175.109.98')
ftp.login(user='whimc-uiuc.129962', passwd='Cr@ft!ng_188P')
source = '/spawn/computercraft/computer'

# Create Snapshot Directory if it doesnt exist
target = 'CC Snapshots'
if not os.path.exists(target):
    os.mkdir(target)

# Continuous Snapshots
print("Press enter to stop taking snapshots!")

keep_going = True


def key_capture_thread():
    global keep_going
    input()
    keep_going = False
    print('Taking last snapshot')


def run():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    while keep_going:
        copy_dir(source, target)
        print('snapshot')
        generate_index_of_names()
        time.sleep(60)


run()

print('Done!')
