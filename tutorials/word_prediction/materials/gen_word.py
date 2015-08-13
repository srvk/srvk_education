#!/usr/bin/python
# -*- coding: utf-8 -*-

import fst
import math

def gen_word_fst (word,isyms=None,osyms=None):
    "This takes a word and creates a transducer from the letters to the word, introducing symbols into the symbol table as needed"
    wordfst=fst.Transducer(isyms,osyms)
    state=0
    for char in word:
        wordfst.add_arc(state,state+1,char,'ε')
        state=state+1
    wordfst[state].final=True
    for arc in wordfst[state-1].arcs:
        arc.olabel=wordfst.osyms[word]
    return wordfst

def create_wordlist_fst (words):
    "This takes a list of words and creates a letter-to-word transducer for all of the words (unioned together)."
    wordset=fst.Transducer();
    for word in words:
        wordfst=gen_word_fst(word,isyms=wordset.isyms,osyms=wordset.osyms)
        wordset=wordset|wordfst
    return wordset

def create_count_array (file):
    "This opens a file, reads the contents, and then stores the contents as a dictionary, indexed by word, with the count of the word"
    count={}
    with open(file) as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in count:
                    count[word]=count[word]+1
                else:
                    count[word]=1
    return count

def sigma (syms):
    "This creates a two-state acceptor that accepts any one letter in isyms"
    thisfst=fst.Acceptor(syms=syms);
    for sym,val in syms.items():
        if (val > 0):
            thisfst.add_arc(0,1,sym)
    thisfst[1].final=True;
    return thisfst

def letter_constraint (letterstring,syms):
    "Create an FSA that has the already typed letters followed by sigma*"
    thisfst=fst.linear_chain(letterstring,syms);
    sigmafst=sigma(syms).closure()
    thisfst.concatenate(sigmafst)
    thisfst.remove_epsilon()
    return thisfst.determinize()

def find_matches1 (letterstring,n=3):
    "Run the whole thing: build the fsts, run the match, return the results"
    counts=create_count_array('brown100')
    dict=create_wordlist_fst(counts.keys())
    let=letter_constraint(letterstring,dict.isyms)
    out=(let>>dict).shortest_path(n)
    
    out.project_output()
    out.remove_epsilon()
    return out

def calculate_unigram_constraint (counts,syms=None):
    probs={}
    total=0
    thisfst=fst.Acceptor(syms=syms)
    for word in counts:
        total+=counts[word]
    for word in counts:
        probs[word]=(counts[word]+0.0)/(total+0.0)
        if (probs[word]<=0.00000000000000001):
            probs[word]=0.00000000000000001
        thisfst.add_arc(0,0,word,-math.log(probs[word]))
    thisfst[0].final=True
    return thisfst

        
        
def find_matches2 (letterstring,n=3):
    "Run the whole thing: build the fsts, run the match, return the results"
    counts=create_count_array('brown100')
    dict=create_wordlist_fst(counts.keys())
    let=letter_constraint(letterstring,dict.isyms)
    uni=calculate_unigram_constraint(counts,dict.osyms)
    out=(let>>dict>>uni).shortest_path(n)
    
    out.project_output()
    out.remove_epsilon()
    return out
