# Labels

**Description:**
--
Here have a some list of resources that described in *targettext_sample.txt*, the main demand for codebase this is ability to select some part of resources and implement some actions for them

For example we have a list and we need to update labels for the first 2 lambda-fix* configmaps, in that case it was  'labelname=value'

**Solution in Bash:**
--
The file **action_targeting.sh** is able to do this using *bash*. Please create a **python** of *js* file with the same functionality

<sub>
An example or output in bash, please update it in python(js):
</sub>

![Screenshot with bash output](https://raw.githubusercontent.com/gruzchik/python_tricks/main/k8s_labeling/example_bash.png)

Steps to reproduce output:

`$ /bin/bash ./action_targeting.sh`

**Task:**
--
Create a *python script*, that will do the same functionality like bash file *action_targeting.sh*:

- [ ] The name should be like ***action_targeting_gitusername.py*** where ***gitusername*** is name of creator

- [ ] Python file should import *targettext_sample.txt* , have ability to choose number of lines that should be updated with a command, and send to output result like we have in Bash script

- [ ] The file should be created in a new branch like *feat/python_gitusername* and create a PR for a **main** branch

Steps to reproduce output:

`$ python3 ./action_targeting.py`
