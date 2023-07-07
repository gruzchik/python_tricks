#!/bin/bash

# k get configmap | while read line; do name=$(echo $line| cut -d " " -f1); if [[ $name == *lambda* ]]; then echo $name; fi ; done
#######
# add label to k8s resoutces with some name
#######

labelname="labelname=value"
count=0
command_input="targettext_sample.txt" # result of kubectl get configmap

cat $command_input | while read line; do
	name=$(echo $line| cut -d " " -f1);
	if [[ $name == *lambda* ]] || [[ $name == *thanks* ]]; then
		echo $name;
		count=$((count+1));
		echo $count;
		if [[ $count -le 1 ]]; then #to how many lines aplly the next command
			echo "kubectl label configmap $name $labelname"
			#kubectl label configmap $name $labelname
		fi
	fi;
done
