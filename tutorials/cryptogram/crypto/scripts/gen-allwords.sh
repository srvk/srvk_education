#!/bin/bash

for i in `cat data/wordlist`; do
  scripts/gen-word.pl $i | fstcompile --isymbols=data/letter.voc --osymbols=data/word.voc - dict/$i.fst
done
