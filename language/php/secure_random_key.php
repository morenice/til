<?php

// not secure hash function
//  - uniqid, like: 4b3403665fea6
printf("uniqid: %s\r\n", uniqid());
printf("uniqid: %s\r\n", uniqid());
printf("uniqid: %s\r\n", uniqid());


// secure hash function
//
$bytes = random_bytes(32);
printf("random_bytes: %s\n", bin2hex($bytes));
$bytes = random_bytes(32);
printf("random_bytes: %s\n", bin2hex($bytes));
$bytes = random_bytes(32);
printf("random_bytes: %s\n", bin2hex($bytes));
