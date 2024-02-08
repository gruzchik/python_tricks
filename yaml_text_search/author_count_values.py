#!/usr/bin/python3

''' checking values in existing containers '''

import yaml

# settings
with open("config_depl_files.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


# count=0
# with open(VALUE_LIST_ZERO,'r') as file:
#     for i in file:
#         if "value:" in i:
#             #print("check.."+i+"\n")
#             i=i.strip()
#             sample=i.split(": ")
#             #print(sample[1])
#             with open(CHECK_LIST1,'r') as file1:
#                 for j in file1:
#                     if "key" in j:
#                         # count=count+1
#                         # print(count)
#                         #print("checking.."+j+"\n")
#                         j=j.strip()
#                         element=j.split(": ")
#                         #print(element[1])
#                         if sample[1] == element[1]:
#                             count=count+1
#                             print(f'value {count}: {element[1]}')
#                             break

def retrieve_setting_values() -> list:
    ''' retrieve values from the settings file '''
    with open(config["settings-file"],'r') as source_file:
        # result = ''
        result = []
        for i in source_file:
            if "secretKey:" in i:
                # result += print("check.."+i+"\n")
                i=i.strip()
                sample=i.split(": ")
                # result += sample[1]+"\n"
                result.append(sample[1])
        return result

def find_declarations():
    ''' find declarations in description file '''
    with open(config["destination-files"],'r') as destination_file:
        result = []
        for j in destination_file:
            if "key:" in j:
                j=j.strip()
                element=j.split(": ")
                result.append(element[1])
        return result

def find_matches(find_items: list, settings_items: list) -> dict:
    ''' find matches in settings and description file '''
    overlap = ''
    count = 0
    # overlap = "\n".join(set(find_items) & set(settings_items))
    # overlap = [x for x in find_items if x in settings_items]
    for item in find_items:
        if item in settings_items:
            count=count+1
            overlap += "value "+str(count)+": "+item+"\n"
    # overlap = "\n".join(overlap)

    return overlap

if __name__ == "__main__":
    setting_values = retrieve_setting_values()
    final_results = find_matches(find_declarations(), retrieve_setting_values())
    # print(setting_values)
    # print(find_declarations())

    print(final_results)
    None