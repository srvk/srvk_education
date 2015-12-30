#!/usr/bin/perl

@letters=('A'..'Z');
@cyphers=('A'..'Z');

while($#cyphers>=0) {
    $r=int(rand($#cyphers+1));
    $l=shift(@letters);
    $c=splice(@cyphers,$r,1);
#    print "$l => $c\n";
    $map{$l}=$c;
}

while(<>) {
    chomp;
    @x=split("",$_);
    @y=&domap(@x);
    print join("",@y),"\n";
}

sub domap {
    return map {(defined($map{$_}))?$map{$_}:$_} @_;
}
