# Labels

**Description:**

Create a Python script that will perform the same functions as *action_targeting.sh*.

The script will work with a file (for example, let's call it *targettext_sample.txt*), that reflects result of the command
```
kubectl create configmap/secret --from file ...
```
and looks like:

```
NAME                    DATA   AGE
someacc-cfg             1      337d
newacc-cfg              1      426d
lambda-fix-3pewGKkCuS   1      455d
lambda-fix-5kChiCqkeh   1      235d
lambda-fix-77JyfH3eEV   1      324d
lambda-fix-T5cAhX7wGg   1      372d
lambda-fix-2FSYKZo7wC   1      363d
lambda-fix-povCG4wP2c   1      355d
lambda-fix-4gcnm5hGFE   1      33d
lambda-fix-DMUW34CHMu   1      26h
lambda-fix-nKG5NdruFa   1      465d
lambda-fix-FuUhpzd786   1      455d
lambda-fix-uG4geEgS7v   1      345d
lambda-fix-N3i5zhe64e   1      339d
thanks-z46q2DDyZF       1      114d
thanks-Ak66bvZotr       1      24h
thanks-4BivxgEya2       1      271d
thanks-4gTrU3U8PY       1      160d
thanks-2UE78SsN6g       1      158d
thanks-wan8wh4ZDU       1      152d
thanks-TRjotz3NrZ       1      245d
thanks-HqcT6B2WoP       1      132d
```

The purpose of the created script is to select lines from the file containing the specified pattern (word) and run a command like:
`kubectl label configmap <`_name_`> <`_label_`>`

Where:
- __label__ - a label that is set explicitly directly in the script text or taken from a separate configuration file.
- __name__ - is the first "word" in the string containing the pattern we are interested in. Let the patterns (list of patterns) be set explicitly directly in the script text or taken from the configuration file.

**Example**
For example, let the *targettext_sample.txt* file contain the patterns of interest to us "lambda-fix" and "thanks". label will be denoted as "labelname".

So the script will have to execute commands in turn:
```
kubectl label configmap lambda-fix-3pewGKkCuS labelname
kubectl label configmap lambda-fix-5kChiCqkeh labelname
[...]
kubectl label configmap thanks-z46q2DDyZF labelname
kubectl label configmap thanks-Ak66bvZotr labelname
[...]
```

Also, the script should be able to limit the number of commands executed.

**Task**
--
- [ ] The name should be like ***action_targeting_gitusername.py***, where ***gitusername*** is the name of the creator.

- [ ] Python script must import *targettext_sample.txt*

- [ ] The Python script should allow you to choose the number of lines from which the patterns will be taken and the command will be run.

- [ ] The Python script should run the command for as many lines as previously selected.

- [ ] The Python script must output (to the screen or to the specified file) the sequence number of the "word" beginning with the pattern and the "word" itself, regardless of whether the command is executed with this "word". The executable command must be output in its entirety.

- [ ] The file must be created in a new branch such as *feat/python_gitusername* and create a PR for the **main** branch

--
Steps to reproduce the output:

`$python3 ./action_targeting.py`







