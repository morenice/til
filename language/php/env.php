<?php

$shell = getenv("SHELL");
echo $shell;
echo "\n";


echo getenv("TEMP_QDFDE24Q");

echo "Put enviroment TEMP_QDFDE24Q\n";
if (!putenv("TEMP_QDFDE24Q=10000"))
{
    echo "Failed put enviroment TEMP_QDFDE24Q\n";
}

echo sprintf("TEMP_QDFDE24Q env: %s\n", getenv("TEMP_QDFDE24Q"));
?>
