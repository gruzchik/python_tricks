#!/usr/bin/env python3

import re


def work_files(filename):
    value_list_zero = None
    output_list = []
    with open(filename) as inf:
        work_list = [line.strip() for line in inf if line != '\n']
    for i in range(1, len(work_list)):
        if work_list[i - 1] == 'Settings file:' and not work_list[i].startswith('#'):
            value_list_zero = work_list[i]
        if work_list[i - 1] == 'File list for checking:' and not work_list[i].startswith('#'):
            output_list.append(work_list[i].split(' #')[0])

    return value_list_zero, output_list


def settings_search(filename):
    pattern = re.compile(r'\bvalue: ?(\w+)\b')
    with open(filename) as inf:
        found = set(pattern.findall(inf.read()))
    return sorted(found)


def deployment_search(check_list, key_list):
    found = []
    for filename in check_list:
        with open(filename, 'r') as inf:
            text = inf.read()
            for elem in key_list:
                pattern = re.compile(fr'\bkey: ?{elem}\b')
                if pattern.search(text):
                    found.append((filename, elem))
    return found


FILENAMES_IN = './files/check_depl_files.lst'
VALUE_LIST_ZERO, CHECK_LIST = work_files(FILENAMES_IN)

key_lst = settings_search(VALUE_LIST_ZERO)
file_lst = deployment_search(CHECK_LIST, key_lst)
[print(f'In {row[0]}\tvalue: {row[1]}') for row in file_lst]
