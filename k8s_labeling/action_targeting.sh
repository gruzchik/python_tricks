#!/bin/bash

# k get configmap | while read line; do pattern=$(echo $line| cut -d " " -f1); if [[ $pattern == *lambda* ]]; then echo $pattern; fi ; done
#######
# add label to k8s resoutces with some pattern
#######

labelname="labelname=value"
count=0
command_output="targettext.txt" # result of kubectl get configmap

cat $command_output | while read line; do 
	pattern=$(echo $line| cut -d " " -f1);
       	if [[ $pattern == *lambda* ]] || [[ $pattern == *tanks* ]]; then
	       echo $pattern;
	       count=$((count+1));
	       echo $count;
               if [[ $count -le 1 ]]; then
	       	  echo "kubectl label configmap $pattern $labelname"
		  #kubectl label configmap $pattern $labelname		
	       fi
	fi;
done
