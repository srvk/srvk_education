# Word Prediction tutorial

This lab was developed as an exercise for OSU CSE 5525: Foundations of Speech and Language Processing.  This is best done after an introduction to the finite state tools is undertaken (e.g. the Cryptography tutorial).  The main premise of this tutorial is to build a system that will allow the user to search for word completions.  Theoretically, it's done by first creating a dictionary converting letter sequences to words, and then composing a constraint fst with the dictionary to find words matching the constraint.  For example, a constraint could be "words beginning with ALL", which would be a FSA with the topology A + L + L + sigma* (where + is concatenation, and sigma* is the closure of all possible letters).  The goal of this tutorial is to give the students more experience in thinking about constraints, to give a bit more practical application than the cryptography demo, and also introduce the idea of probabilities which can be useful for the LM and Kaldi tutorials.

Software requirements
=====================
* OpenFST (should be installed in VM)
* PyFST (should be installed in VM)
* ipython + ipython notebook (should be installed in VM)

Data requirements
=================
* brown100, brown1000, test (in this directory)

How to get started
==================
* See WordPredictionTutorial.pdf to get started

TO DO
=====

NOTES 
===== 
Requires some familiarity with python to follow my
solution.  Can also just be done using command line scripts but some
sort of coding is really necessary to create sigma, for example.
