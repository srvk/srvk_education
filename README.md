# srvk_education
Educational tutorials for speech and language processing classes

This repository contains materials that can be utilized in in-class tutorials for speech and language processing classes.
The original material in this repository comes from CSE 5525: Foundations of Speech & Language Processing at The Ohio State University.

The material in this repository is geared towards advanced undergraduates and graduate students.  Many of the tutorials assume a
programming background, and at least a passing familiarity with python.

A virtual machine is used to house the resources; this VM can be built using Vagrant.  After installing vagrant, issuing “vagrant up” in the directory where the Vagrantfile is will create a new VM with all of the materials.

Note that this version has some missing data that is commonly available in the speech community, which can be installed in a directory called "protected" parallel to the Vagarant file *before* initializing the vagrant vm.  As of now, there are four protected data sources:

* labeling_lab: contains sentences from TIMIT converted into audacity format.  samp_sa1.aup contains one version of "She held your dark suit in greasy wash water all year" with labels.  sa1.aup cotains another version of the same sentence from another speaker, but without labels (but word labels) for students to label.  sa2.aup contains a different sentence.

* lm_lab: contains the 5k language model data from WSJ0.  Can easily be replaced with other free data.

* srilm-1.7.1.tar.gz: contains a downloaded version of SRILM (which is free for instructional purposes but must be downloaded from SRI - web search for "srilm toolkit" to find the current version.  You will need to change the Vagrantfile to reflect the current version.

* tidigits.tgz: contains a copy of the TIDIGITS database, using the following ordering

bash-3.2$ tar -tzf protected/tidigits.tgz | head
tidigits/
tidigits/data/
tidigits/data/adults/
tidigits/data/adults/test/
tidigits/data/adults/test/man/
tidigits/data/adults/test/man/ah/
tidigits/data/adults/test/man/ah/111a.wav
tidigits/data/adults/test/man/ah/139oa.wav
tidigits/data/adults/test/man/ah/155a.wav
tidigits/data/adults/test/man/ah/1688a.wav

If you have licenses for WSJ, TIMIT or TIDIGITS and would like to know how to create the files needed for the experiments, please contact Eric Fosler-Lussier.  

TO DO: rewrite tutorials using licensed data/toolkits with open data and toolkits.