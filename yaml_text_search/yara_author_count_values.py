#!/usr/bin/env python3

"""    Identifying files containing interests us patterns     """

import re
import sys
import yaml


def work_names(filename: str) -> tuple:
    """    Extract file names to parse and word after which script need to look for a pattern    """
    with open(filename, encoding='utf-8') as inf:
        config = yaml.load(inf, Loader=yaml.FullLoader)
    value_list_zero = config.get('settings-file')
    output_list = config.get('destination-files')
    key_word = config.get('search-settings-pattern')
    return value_list_zero, output_list, key_word


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


FILENAMES_IN = './config_depl_files.yaml'
VALUE_LIST_ZERO, CHECK_LIST, MATCH_AFTER_WHICH = work_names(FILENAMES_IN)

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
