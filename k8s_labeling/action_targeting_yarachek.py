#!/usr/bin/python3

"""
Script modifies the command
$ kubectl label configmap
"""

import subprocess
import traceback
import datetime


def command(name, names_number, label):
    """
    Function modifies the command
    $ kubectl label configmap
    and adds information about errors that occur when executing the modified command -> log file

    :param name: first “word” in the string containing the pattern we are interested in
    :param names_number: ordinal number of the “word” we encounter
    :param label: last argument in modified command
    :return: nothing
    """
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
LABEL_NAME = "labelname=value"
COMMAND_INPUT = 'targettext_sample.txt'
ERRORS_LOG = 'errors.log'
runtime_limit: int = 3  # number of commands to be executed
patterns = ('lambda',
            'thanks'
            )
# end of block with information that can be taken from separate file(s)

with open(COMMAND_INPUT, 'r', encoding='utf-8') as inf,\
        open(ERRORS_LOG, 'a', encoding='utf-8') as ouf:
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
                command(argument, arguments_number, LABEL_NAME)
