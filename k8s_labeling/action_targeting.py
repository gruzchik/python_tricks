#!/usr/bin/python3

import subprocess
import traceback
import datetime


def command(name, names_number, quantity):
    print(f'kubectl label configmap {name} x {quantity} time(s)')
    for _ in range(quantity):
        try:
            subprocess.call(["kubectl label configmap", name])
        except:
            print(f'Error lable:{names_number}\n'
                  f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}:\n'
                  f'Error while executing "kubectl label configmap {name}"\n'
                  f'{traceback.format_exc()}\n', file=ouf)


with open('targettext_sample.txt', 'r', encoding='utf-8') as inf,\
        open('errors.log', 'a', encoding='utf-8') as ouf,\
        open('runtime_limit', 'r', encoding='utf-8') as rtl:

    runtime_limit = rtl.readline().strip().split()[2]
    arguments_number = 0
    runtime_number: int = 0

    try:
        runtime_limit = int(runtime_limit)
    except:
        print('Runtime limit is not number. Please check file "runtime_limit"')
        exit()

    for line in inf:
        argument = line.strip().split()[0]
        data = line.strip().split()[1]

        if data.isdigit():

            if argument[:10] == 'lambda-fix' or argument[:6] == 'thanks':
                try:
                    data = int(data)
                    arguments_number += 1
                    print(arguments_number)
                    print(argument)
                    runtime_number += 1
                    if data >= 0 and 0 <= runtime_number <= runtime_limit:
                        command(argument, arguments_number, data)
                except:
                    pass
