#!/usr/bin/perl

while(<>) {
    # line is stored in $_
    chomp($_);             # get rid of trailing newliens
    $_=~tr/a..z/A..Z/;     # change everything to upppercase

    $_=~s/[^A-Z]//g;       # get rid of characters not between A and Z
    @chars=split("",$_);   # break up char into array x, one char per element
                           # e.g. split("","ABC") produces ("A","B","C")

    foreach $letter (@chars) {
	$count{$letter}++; # increment the hash $count{"A"}, for example
	$total++;          # keep track of the total # of characters
    }
}

foreach $letter ("A".."Z") {  # go through all of the letters
    printf("%s %.6f\n",$letter,$count{$letter}/$total);
}
