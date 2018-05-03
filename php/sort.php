<?php

$a = [
    ['k1' => 'a1', 'b'=> 'b', 'c'=> 0.4],
    ['k2' => 'a2', 'b'=> 'b', 'c'=> 1.4],
    ['k3' => 'a3', 'b'=> 'b', 'c'=> 2.0],
    ['k4' => 'a4', 'b'=> 'b', 'c'=> 0.8]
];

usort($a, function ($a, $b)
{
    if ($a['c'] == $b['c']) {
        return 0;
    }
    return ($a['c'] < $b['c']) ? -1 : 1;
});

foreach ($a as $i) {
    var_dump($i);
}

