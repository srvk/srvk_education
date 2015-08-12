# Phone Labeling Lab

This lab was developed as an exercise for OSU CSE 5525: Foundations of Speech and Language Processing.  The primary idea of this tutorial is to get students to look at spectrograms and listen to speech data to understand the variety of speech patterns there are, even within one speaker.  Students find this very challenging, but by the end of class tend to appreciate the variation in speech.

Software requirements
=====================
* Audacity (should be installed in VM)

Data requirements
=================
* TIMIT audacity data package: note that this is data licensed from the LDC but has been packaged for the class.  Contact the author, Eric Fosler-Lussier (fosler@cse.ohio-state.edu) to obtain the packaged data if you have licensed TIMIT from the LDC.
* phone_labeling_instructions.pdf: a how-to guide on getting started
* timit_symbols.pdf: a page from Eric Fosler-Lussier’s PhD thesis showing the labels used in TIMIT as well as example words

How to get started
==================
* Build the virtual machine
* Place the data in the right place (more detail needed here)
* “vagrant ssh” to open a connection to the system
* “audacity” to get audacity running
* open the audacity project file as mentioned in the pdf reader

TO DO
=====
Create a version of this tutorial using open source materials, likely from the Buckeye Corpus of Speech.

NOTES
=====
Audacity can be very finicky when run in the virtual machine.  In particular, it sometimes has trouble finding a low-latency audio driver.  Generally you will want to pick the audio driver that is closest to the hardware.  On my mac, it sometimes requires starting and quitting audacity in the VM to find the appropriate driver.  Pulse audio tends to be problematic on my mac.

Since Audacity is available for Windows, Linux, and Mac, you can download it onto a machine and just use the files, ignoring the VM, if you find that audacity is not working well within the VM.