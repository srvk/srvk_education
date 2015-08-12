# Kaldi TIDigits tutorial   

This elaborates on the tidigits tutoral that is found in the main distribution of Kaldi, giving a bit more of a walkthrough on what appears in run.sh.  The VM is set up to adjust the Kaldi scripts to be a bit more suited to running in a virtual environment (e.g. reducing the number of jobs to 2 rather than 20).  

Software requirements
=====================
* Kaldi (should be installed in VM)

Data requirements
=================
* Tidigits data package: note that this is data licensed from the LDC so it is not included here.  Only the adult data are used.  The directory layout used by Kaldi is "tidigits/data/adults/test/man/ah/111a.wav", for example.

How to get started
==================
* Place the data into protected/tidigits.tgz
* Build the virtual machine (will copy the tidigits data into the right place)
* “vagrant ssh” to open a connection to the system
* Follow the instructions in Kaldi_tutorial.pdf

TO DO
=====
* Right now the version of the tutorial instructions says "/home/mario" rather than "/home/vagrant".  Needs to be fixed.
* Version using open source data (ICSI Meeting Recorder)

NOTES
=====
Kaldi can be a bit a of a slow go on slower laptops, so following instructions on "what to look at" can help use the time wisely.  
