#!/usr/bin/python3

import subprocess
import traceback
import datetime


def command(name, names_number, label):
    to_exec = 'kubectl label configmap ' + name
    print(f'{to_exec} {label}')
    try:
        subprocess.call([to_exec, label])  # If it does not work in this form, do this:
#       subprocess.call(["kubectl label configmap", " ".join((name, label))])

    except:
        print(f'Error while attempt #{names_number}\n'
              f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}:\n'
              f'Error while executing "{to_exec}"\n'
              f'{traceback.format_exc()}\n', file=ouf)


# start of block with information that can be taken from separate file(s)
labelname = "labelname=value"
command_input = 'targettext_sample.txt'
errors_log = 'errors.log'
runtime_limit: int = 3  # number of commands to be executed
patterns = ('lambda',
            'thanks'
            )
# end of block with information that can be taken from separate file(s)

with open(command_input, 'r', encoding='utf-8') as inf, open(errors_log, 'a', encoding='utf-8') as ouf:
    arguments_number: int = 0
    runtime_number: int = 0

    for line in inf:
        argument = line.strip().split()[0]

        if argument.startswith(patterns):
            arguments_number += 1
            runtime_number += 1
            print(arguments_number)
            print(argument)
            if runtime_number <= runtime_limit:
                command(argument, arguments_number, labelname)
