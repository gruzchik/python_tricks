#!/usr/bin/python3

''' checking values in existing containers '''

import yaml

# settings file
with open('config_depl_files.yaml', 'r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

def retrieve_setting_values() -> list:
    ''' retrieve values from the settings file '''
    with open(config['settings-file'], 'r', encoding='utf-8') as source_file:
        result = []
        for i in source_file:
            if "{}:".format(config['search-settings-pattern']) in i:
                i=i.strip()
                sample=i.split(": ")
                result.append(sample[1])
        return result

def find_declarations():
    ''' find declarations in description file '''
    result = []
    for file_for_parsing in config['destination-files']:
        with open(file_for_parsing, 'r', encoding='utf-8') as destination_file:
            for j in destination_file:
                if "{}:".format(config['search-deployment-pattern']) in j:
                    j=j.strip()
                    element=j.split(": ")
                    if element[1] not in result:
                        result.append(element[1])
    return result

def find_matches(find_items: list, settings_items: list) -> dict:
    ''' find matches in settings and description file '''
    overlap = []
    for item in find_items:
        if item in settings_items:
            overlap.append(item)
    return overlap

if __name__ == "__main__":
    setting_values = retrieve_setting_values()
    final_results = find_matches(find_declarations(), retrieve_setting_values())
    # print(setting_values)
    # print(find_declarations())

    # print(final_results)
    COUNT=0
    for final_line in final_results:
        COUNT=COUNT+1
        print("value {}: {}".format(str(COUNT), final_line))
