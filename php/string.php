<?php

$parse_str1  = "piece1, piece2, piece3, piece4";
$pieces = explode(",", $parse_str1);

foreach ($pieces as $piece) {
    print trim($piece);
    print "\n";
}

$parse_str2  = "";
$pieces = explode(",", $parse_str2);

// array 1 (empty)
foreach ($pieces as $piece) {
    print trim($piece);
    print "\n";
}

$v = is_numeric('1232131') ? true : false;
print $v;
print "\n";
