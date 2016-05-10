#!/bin/zsh

VAR1=1
while [ $VAR1 -lt 101 ]
do 
    echo "value of VAR1 is : $VAR1"
    ((VAR1=VAR1+1))
done
