#!/bin/bash

# create an alias to emulate kubectl command
alias kubectl='/bin/bash ./generate_configmap_mock.sh'

# remove alias to restore work with real kubectl
# unalias kubectl
