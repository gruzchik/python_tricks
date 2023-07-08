import subprocess
import os

# settings
labelname="labelname=value"
command_input="targettext_sample.txt" # result of kubectl get configmap
cycle_quantity="5"


bash_command="kubectl get configmap"

# Opening file
input_file = open(command_input, 'r')
count = 0
 
# Using for loop
print("Using for loop")
for line in input_file:
    name=line.split()[0]
    # print("Line{}: {}".format(count, line.strip()))
    if "lambda" in name:
        if int(cycle_quantity) >= count:        
            print("kubectl configmap label " +name+ " " +labelname)
            

        count += 1
        print(name)   
        print(count)
    
# Closing files
input_file.close()