#!/usr/bin/perl

# useful constants
$pi=atan2(1,1)*4;
$sqrt2pi=sqrt(2*$pi);
$cutoff=0.0001;

if ($#ARGV<1 || $#ARGV>2) {
    print STDERR "Usage: $0 english_letter_stats_file crypt_stats_file [hypothesis_file]\n";
    exit;
}

#
# read in letter statistics
#

open(LETTERSTATS,$ARGV[0]) || die("Can't open $ARGV[0] for reading");

while(<LETTERSTATS>) { # read each line and put it into $_

    chomp;                   # get rid of newlines
    ($letter,$mean,$std)=split(/\s+/,$_);
                             # split the line into three parts based on 
                             # whitespace

    $mean{$letter}=$mean;    # store the mean in a hashtable
    $std{$letter}=$std;      # store the standard deviation in a hashtable
}

close(LETTERSTATS);

#
# read in hypothesis (if any)
#

if (defined($ARGV[2])) {     # if there is a hypothesis file
    open(HYPOTHESIS,$ARGV[2]);
    while(<HYPOTHESIS>) {
	chomp;               # get rid of newlines
	($crypt,$actual)=split(/\s+/,$_);  # get the crypt and actual letters
	$hyp{$crypt}=$actual;   #store it in a hashtable
	$revhyp{$actual}=$crypt;
   }
    close(HYPOTHESIS);
}


open(CRYPTSTATS,$ARGV[1]) || die("Can't open $ARGV[1] for reading");
while(<CRYPTSTATS>) {   # get lines one at a time and put into $_
    chomp;               # get rid of newlines
    ($letter,$mean)=split(/\s+/,$_);  # get the letter and mean (sep by spaces)
    if (defined($hyp{$letter})) {   # if we have a hypothesis already, just 
	                            # print that out instead
	print "0 0 $letter $letter$hyp{$letter} 0\n";
    } else {
	foreach $hypletter ("A".."Z") {
	    next if (defined($revhyp{$hypletter}));
	    $prob=&probability($mean,$hypletter);
	    if ($prob>$cutoff) {
		printf("0 0 %s %s%s %.6f\n",$letter,$letter,$hypletter,&neglog($prob));
	    }
	}
    }
}
close(CRYPTSTATS);
print "0 0 \# \# 0\n";
print "0\n";

# function to compute probability
sub probability {
    my $mean=shift(@_);
    my $hypletter=shift(@_);
    
    my $hypmean=$mean{$hypletter};
    my $hypstd=$std{$hypletter};

#    print "$mean $hypmean $hypstd $hypletter\n";

    return 1/($hypstd*$sqrt2pi) * exp(-($mean-$hypmean)**2/(2*$hypmean**2));
}

# function to compute the negative logarithm
sub neglog {
    if ($_[0]==0) {
	return "Inf";
    } else {
	return -log($_[0]);
    }
}
