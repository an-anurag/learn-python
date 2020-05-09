"""Automator"""

import os
import shutil
import re


def folder_copier(source, dest):
    """
    Copies all the files in given source location to destination location.
    Checks if file already exist
    :param source: directory location to start copy from
    :param dest: directory location to copy files into.
    :return:
    """

    i = '_renamed'
    for file in os.listdir(source):
        dir_name = dest.split('/')[-1]

        if not os.path.exists(os.path.join(dest, file)):
            shutil.copy2(os.path.join(source, file), os.path.join(dest, file))
            print(f"{file} copied")
            print(f"{len(os.listdir(source))} Files copied successfully to {dir_name}")

        else:
            print(f"{file} File already exists, tell me what to do:\n")
            ch = int(input("PRESS \t 1 - Rename & Copy \n"
                           "\t\t 2 - Skip file\n"))
            if ch == 1:
                name, ext = os.path.splitext(file)
                os.rename(os.path.join(source, file), os.path.join(source, name + i + ext))
                print(f"{file} is renamed and copied")
                for new_file in os.listdir(source):
                    shutil.copy2(os.path.join(source, new_file), os.path.join(dest, new_file))

            if ch == 2:
                print(f"{file} is skipped")
                continue


def root_directory(root, new_ext):
    """
    this changes extension of files in source directory and
    ignore the subdirectories and their files.
    :param root: source path to start file renaming
    :param new_ext: new file extension to be applied
    :return:
    """
    file_list = []
    for file in os.listdir(root):
        if os.path.isfile(file):
            file_path = os.path.join(root, file)
            print(file_path)
            file_list.append(file_path)
            file_name, old_ext = os.path.splitext(file)
            os.rename(file_path, os.path.join(root, file_name + new_ext))
            print(file_path)

    print(f'Renamed {len(file_list)} files with {new_ext} extension')


def multi_directory(root, new_ext):
    """
    This changes extension of files contained in all the subdirectories present in the source folder.
    it ignores the source folder
    :param root: source path to start file renaming
    :param new_ext: new file extension to applied
    :return:
    """
    regex = re.compile('[.]')

    file_list = []
    for directory in os.listdir(root):
        if os.path.isdir(directory):
            dir_path = os.path.join(root, directory)

            for file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file)
                print(file_path)
                file_list.append(file_path)
                file_name, ext = os.path.splitext(file_path)

                if regex.search(file_name):
                    print('File already exists')
                    new_name = input(str('Enter new name for the file without extension: \n'))
                    os.rename(file_path, os.path.join(dir_path, new_name + new_ext))

                else:
                    os.rename(file_path, os.path.join(file_path, file_name + new_ext))
    print(f'Renamed {len(file_list)} files with {new_ext} extension')


def start_folder_copier():
    print('#' * 50)
    print("ATUOMATIC FOLDER COPIER".center(50))
    print('#' * 50)
    source = str(input("Enter source path:\n"))
    dest = str(input("Enter destination path: \n"))
    folder_copier(source, dest)


def start_extension_changer():
    print('#' * 50)
    print("BATCH FILE EXTENSION CHANGER".center(50))
    print('#' * 50)
    root = str(input("Enter directory location to proceed...\n"))
    print(f'Selected Location:\n{root}')
    print()

    dir_count = [item for item in os.listdir(root) if os.path.isdir(item)]
    print(f'Total folder(s) found: {len(dir_count)}')
    file_count = [item for item in os.listdir(root) if os.path.isfile(item)]
    print(f'Total files(s) found: {len(file_count)}')
    print(os.listdir(root))

    flag = True
    while flag:
        print()
        choice = int(input("Select operation mode\n"
                           "PRESS 1 - for root directory mode\n"
                           "PRESS 2 - for tree directory mode\n"
                           "PRESS 0 - quit\n"))

        if choice == 1:
            ext = input(str("Enter new file extension (eg: '.jpg'): \n"))
            root_directory(root, ext)

        elif choice == 2:
            ext = input(str("Enter new file extension (eg: '.jpg'): \n"))
            multi_directory(root, ext)

        elif choice == 0:
            flag = False
            print("Exiting...")
        else:
            print("Invalid choice")


if __name__ == '__main__':
    print('#' * 50)
    print("AUTOMATER".center(50))
    print('#' * 50)
    print("Choose your task")
    choice = int(input("PRESS\t 1 - Folder Copier\n"
                       "\t\t 2 - Extension Changer\n"))

    if choice == 1:
        start_folder_copier()

    elif choice == 2:
        start_extension_changer()
