#!/usr/bin/env python3

"""    Identifying files containing interests us patterns     """

import re
import sys


def work_files(filename: str) -> tuple:
    """    Extract file names to parse    """
    with open(filename, encoding='utf-8') as inf:
        work_list = [line.strip() for line in inf if line != '\n' and not line.startswith('#')]
    value_list_zero = work_list[work_list.index('Settings file:') + 1]
    output_list = work_list[work_list.index('File list for checking:') + 1:]
    output_list = [elem.split('#')[0].strip() for elem in output_list]
    return value_list_zero, output_list


def settings_search(filename: str, keyword: str) -> list:
    """    Searching for patterns in a settings file    """
    pattern = re.compile(fr'\b{keyword}: ?(\w+)\b')
    with open(filename, encoding='utf-8') as inf:
        found = set(pattern.findall(inf.read()))
    return sorted(found)


def deployment_search(filename: str, key_list: list) -> list:
    """    Searching for patterns in a deployments file    """
    with open(filename, encoding='utf-8') as inf:
        text = inf.read()
        found = [elem for elem in key_list if re.search(fr'\bkey: ?{elem}\b', text)]
    return found


def result_deployment_search(check_list: list, key_list: list) -> dict:
    """    Creating a dictionary with file names and patterns in them    """
    found = {filename: deployment_search(filename, key_list) for filename in check_list}
    return found


FILENAMES_IN = './files/check_depl_files'

with open('./files/match_after_which', encoding='utf-8') as word:
    MATCH_AFTER_WHICH = word.read().strip()

VALUE_LIST_ZERO, CHECK_LIST = work_files(FILENAMES_IN)

key_lst = settings_search(VALUE_LIST_ZERO, MATCH_AFTER_WHICH)
if not key_lst:
    print(f'No settings (value) in "{VALUE_LIST_ZERO}"')
    sys.exit()

file_lst = result_deployment_search(CHECK_LIST, key_lst)
for key, values in file_lst.items():
    if not values:
        print(f'In file "{key}" no deployment keys')
    else:
        for value in values:
            print(f'In file "{key}"\tvalue: {value}')
