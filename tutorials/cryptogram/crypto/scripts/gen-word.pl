#!/usr/bin/perl

$_=$ARGV[0];

s/[^A-Z\#]//g;
@x=split("");
$ct=0;
$wd=$_;
foreach $x (@x) {
    printf("%d %d %s %s\n",$ct,$ct+1,$x,$wd);
    $wd="-";
    $ct++;
}
print "$ct\n";

	
