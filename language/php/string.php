<?php

$parse_str1  = "piece1, piece2, piece3, piece4";
$pieces = explode(",", $parse_str1);

// split string to array
foreach ($pieces as $piece) {
    print trim($piece);
    print "\n";
}

$parse_str2  = "";
$pieces = explode(",", $parse_str2);

// split empty case
foreach ($pieces as $piece) {
    print trim($piece);
    print "\n";
}

// is num value string
$v = is_numeric('1232131') ? true : false;
print $v;
print "\n";

// string formating
print sprintf("%s %d\n", "This is", 3);

