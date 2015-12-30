#!/usr/bin/perl

$file=$ARGV[0];
foreach $letter ("A".."Z") {
    $doitstr.="fsmintersect fwdconstr/$letter.fsa $file | fsmdeterminize | fsmminimize ";
    $doitstr.="| fsmintersect revconstr/$letter.fsa $file | fsmdeterminize | fsmminimize ";
    if ($letter ne "Z") {
	$doitstr.="|";
    }
    $file="-"
}

system($doitstr);
