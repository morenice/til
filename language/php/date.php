<?php

$date1 = date("Y-m-d H:i:s");
print($date1);
print("\n");

$date2 = strtotime("now");
print($date2);
print("\n");
print(strtotime($date1 . "+3days"));
