#!/usr/bin/python

# settings
labelname="labelname=value"
command_input="targettext_sample.txt" # result of kubectl get configmap
cycle_quantity="3"


bash_command="kubectl get configmap"

# Opening file
input_file = open(command_input, 'r')
count = 0

# Using for loop
print("Using for loop")
for line in input_file:
    name=line.split()[0] # name of configmap
    if "lambda" in name or "thanks" in name:
        count += 1
        if int(cycle_quantity) >= count:
            print("kubectl configmap label " +name+ " " +labelname)
        print(name)
        print(count)

# Closing files
input_file.close()
