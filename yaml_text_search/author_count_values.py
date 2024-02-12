#!/usr/bin/python3

''' checking values in existing containers '''

import yaml

# settings file
with open("config_depl_files.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

def retrieve_setting_values() -> list:
    ''' retrieve values from the settings file '''
    with open(config["settings-file"],'r') as source_file:
        result = []
        for i in source_file:
            if "{}:".format(config["search-settings-pattern"]) in i:
                i=i.strip()
                sample=i.split(": ")
                result.append(sample[1])
        return result

def find_declarations():
    ''' find declarations in description file '''
    for file_for_parsing in config["destination-files"]:
            with open(file_for_parsing,'r') as destination_file:
                result = []
                for j in destination_file:
                    if "{}:".format(config["search-deployment-pattern"]) in j:
                        j=j.strip()
                        element=j.split(": ")
                        result.append(element[1])
                return result

def find_matches(find_items: list, settings_items: list) -> dict:
    ''' find matches in settings and description file '''
    overlap = []
    count = 0
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
    count=0
    for i in final_results:
        count=count+1
        print("value {}: {}".format(str(count), i))
    None