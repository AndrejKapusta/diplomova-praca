#!/bin/bash

for i in *.wav;
do 
echo $i; sox "$i" -e signed-integer -b 16 -r 16000 -c 1 ${i%%.wav}.new.wav;
done

