#!/bin/bash

scripts/gen-word.pl `sed -e 's/  */\#/g' -e 's/ *$/\#/' $1` | \
  gawk 'NF==4 {$4=""} {print}'

