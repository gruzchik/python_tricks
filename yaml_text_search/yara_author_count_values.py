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
    search_settings_pattern = config.get('search-settings-pattern')
    search_deployment_pattern = config.get('search-deployment-pattern')
    return value_list_zero, output_list, search_settings_pattern, search_deployment_pattern


def settings_search(filename: str, keyword: str) -> list:
    """    Searching for patterns in a settings file    """
    pattern = re.compile(fr'\b{keyword}: ?(\w+)\b')
    with open(filename, encoding='utf-8') as inf:
        found = set(pattern.findall(inf.read()))
    return sorted(found)


def deployment_search(filename: str, key_list: list, keyword: str) -> list:
    """    Searching for patterns in a deployments file    """
    with open(filename, encoding='utf-8') as inf:
        text = inf.read()
        found = [elem for elem in key_list if re.search(fr'\b{keyword}: ?{elem}\b', text)]
    return found


def result_deployment_search(check_list: list, key_list: list, keyword: str) -> dict:
    """    Creating a dictionary with file names and patterns in them    """
    found = {filename: deployment_search(filename, key_list, keyword) for filename in check_list}
    return found


FILENAMES_IN = './config_depl_files.yaml'
VALUE_LIST_ZERO, CHECK_LIST, SEARCH_SETTINGS_PATTERN, SEARCH_DEPLOYMENT_PATTERN = \
    work_names(FILENAMES_IN)

key_lst = settings_search(VALUE_LIST_ZERO, SEARCH_SETTINGS_PATTERN)
if not key_lst:
    print(f'No settings (value) in "{VALUE_LIST_ZERO}"')
    sys.exit()

file_lst = result_deployment_search(CHECK_LIST, key_lst, SEARCH_DEPLOYMENT_PATTERN)
for key, values in file_lst.items():
    if not values:
        print(f'In file "{key}" no deployment keys')
    else:
        for value in values:
            print(f'In file "{key}"\tvalue: {value}')
