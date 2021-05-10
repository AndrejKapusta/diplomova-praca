#!/bin/bash

cat corpus.txt | tr -s " " | tr -s " " "\n" | sort | grep "[[:alnum:]]" | uniq -c | tr -s " " | cut -d " " -f 3- > words-new.txt
