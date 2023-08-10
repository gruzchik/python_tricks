#!/bin/bash

if [[ $1 != 'get' ]] || [[ $2 != 'configmap' ]]; then
	exit
fi

LAMBDA_FIX_QUANTITY=5
THANKS_QUANTITY=8

echo "NAME                      DATA   AGE"
echo "someacc-cfg        1      422d"
echo "newacc-cfg        1      422d"

for ((n=0;n<${LAMBDA_FIX_QUANTITY};n++)); do
	RANDOM_HASH_L=$(head -c 100 /dev/urandom | tr -dc a-zA-Z0-9 | fold -w 10 | head -n 1)
	RANDOM_DAYS_L=$((1 + $RANDOM % 300))	
	echo "lambda-fix-${RANDOM_HASH_L}   1      ${RANDOM_DAYS_L}d"
	# echo "lambda-fix-11111   1      ${RANDOM_DAYS_L}d"
done

for ((n=0;n<${THANKS_QUANTITY};n++)); do
    #     RANDOM_HASH_T=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
        RANDOM_DAYS_T=$((1 + $RANDOM % 300))	
	# echo "thanks-${RANDOM_HASH_T}          1      ${RANDOM_DAYS_T}d"
	echo "thanks-222          1      ${RANDOM_DAYS_T}d"
done
