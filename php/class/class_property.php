<?php

class Any
{
    public $sample = 0;
}

$a = new Any();

print($a->sample);

// dynamic property declar
$a->sample2 = 1;
print($a->sample2);
