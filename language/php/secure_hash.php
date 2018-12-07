<?php

$password = "1a5k*@$%";
$hash_result = hash("sha256", $password);

echo sprintf("password: %s\r\n", $password);
echo sprintf("sha256 hash: %s\r\n", $hash_result);
?>
