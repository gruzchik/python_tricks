#!/usr/bin/python3

''' checking values in existing containers '''

# settings

VALUE_LIST_ZERO=f"files/settings.yaml" # list of external values
CHECK_LIST1=f"files/deployment.yaml" # deployment with values
# CHECK_LIST2=f"overlays/sandbox/deployment-patch.yaml" # deployment with values
# CHECK_LIST3=f"overlays/alpha/deployment-patch.yaml" # deployment with values
# CHECK_LIST4=f"overlays/beta/deployment-patch.yaml" # deployment with values


count=0

with open(VALUE_LIST_ZERO,'r') as file: 
    for i in file:
        if "value:" in i:
            #print("check.."+i+"\n")
            i=i.strip() 
            sample=i.split(": ")
            #print(sample[1])
            with open(CHECK_LIST1,'r') as file1:
                for j in file1:
                    if "key" in j:
                        # count=count+1
                        # print(count)
                        #print("checking.."+j+"\n")
                        j=j.strip() 
                        element=j.split(": ")
                        #print(element[1])
                        if sample[1] == element[1]:
                            count=count+1
                            print(f'value {count}: {element[1]}')
                            break

