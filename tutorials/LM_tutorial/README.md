# Language Modeling Tutorial

The language modeling tutorial uses SRILM to train and examine language models.  The purpose of the tutorial is to allow students to understand the idea of backoff and discounting.

Software requirements
=====================
* SRILM (should be installed in VM if present in protected folder)

Data requirements
=================
* WSJtrain, WSJtest (should be installed in VM if present in protected folder)

How to get started
==================
* Read LM_tutorial.pdf for the walk through of the tutorial.

TO DO
=====
* Provide tutorial using non-licensed data
* Use alternate open-source LM toolkit to facilitate license issues
* Re-incorporate lattice rescoring tutorial

NOTES 
===== 
For this tutorial, WSJtrain and WSJtest can be replaced with any two
data files of sufficient length.  It's recommended that the text be
normalized (for example, translated to all uppercase) so that students
new to language models don't need to think about that.  

Originally there was a lattice rescoring tutorial that accompanied
this tutorial, which required the use of the WSJ data.  This is being
redeveloped.

