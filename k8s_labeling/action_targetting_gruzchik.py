#!/usr/bin/python

# settings
LABELNAME="labelname=value"
COMMAND_INPUT="targettext_sample.txt" # result of kubectl get configmap
CYCLE_QUANTITY="3"


BASH_COMMAND="kubectl get configmap"

# Opening file
input_file = open(COMMAND_INPUT, 'r')
COUNT = 0

# Using for loop
print("Using for loop")
for line in input_file:
    name=line.split()[0] # name of configmap
    if "lambda" in name or "thanks" in name:
        COUNT += 1
        if int(CYCLE_QUANTITY) >= COUNT:
            print("kubectl configmap label " +name+ " " +LABELNAME)
        print(name)
        print(COUNT)

# Closing files
input_file.close()
