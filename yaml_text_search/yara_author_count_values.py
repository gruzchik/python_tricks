#!/usr/bin/env python3

import re


def work_files(filename):
    """
    Extract file names to parse
    """
    value_list_zero = None
    output_list = []
    with open(filename, encoding='utf-8') as inf:
        work_list = [line.strip() for line in inf if line != '\n']
    for i in range(1, len(work_list)):
        if work_list[i - 1] == 'Settings file:' and not work_list[i].startswith('#'):
            value_list_zero = work_list[i]
        if work_list[i - 1] == 'File list for checking:' and not work_list[i].startswith('#'):
            output_list.append(work_list[i].split(' #')[0])

    return value_list_zero, output_list


def settings_search(filename, keyword):
    """
    Parsing settings file
    :param filename: file which may contain settings
    :param keyword: the word after which you need to look for a pattern
    :return: found patterns
    """
    pattern = re.compile(fr'\b{keyword}: ?(\w+)\b')
    with open(filename, encoding='utf-8') as inf:
        found = set(pattern.findall(inf.read()))
    return sorted(found)


def deployment_search(check_list, key_list):
    """
    Parsing deployments file
    :param check_list: list of files to parsing
    :param key_list: list of patterns to look for
    :return: file names and found patterns
    """
    found = {filename: [] for filename in check_list}
    for filename in check_list:
        with open(filename, encoding='utf-8') as inf:
            text = inf.read()
            for elem in key_list:
                pattern = re.compile(fr'\bkey: ?{elem}\b')
                if pattern.search(text):
                    found[filename].append(elem)
    return found


FILENAMES_IN = './files/check_depl_files.lst'
MATCH_AFTER_WHICH = 'value'

VALUE_LIST_ZERO, CHECK_LIST = work_files(FILENAMES_IN)

key_lst = settings_search(VALUE_LIST_ZERO, MATCH_AFTER_WHICH)

if len(key_lst) < 1:
    print(f'No settings (value) in "{VALUE_LIST_ZERO}"')
    exit()

file_lst = deployment_search(CHECK_LIST, key_lst)
for key, values in file_lst.items():
    if len(values) < 1:
        print(f'In file "{key}" no deployment keys')
    else:
        for value in values:
            print(f'In file "{key}"\t value: {value}')
