#!/bin/bash

count=0
cat files/deployment.yaml| grep key|cut -d ":" -f2 > 1.txt

cat files/settings.yaml | grep value| cut -d ":" -f2| while read line; do
	#echo "check $line ...";
	for i in $(cat 1.txt)
	do
		#count=$((count+1))
		#echo $count

		#echo "element = $i"
		if [[ $i == $line ]]
		then
			count=$((count+1))
			echo "value $count: $line" && break
		fi


	done
done
