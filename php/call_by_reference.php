<?php

class Dummy
{
    public $d1;
}

class A
{
    private $a1;
    private $a2;

    public function setA1($val)
    {
        $this->a1 = $val;
    }

    public function getA1()
    {
        return $this->a1;
    }

    public function assignArg($arg)
    {
        echo "assignArg:\n";
        $arg = $this->a1;
    }

    public function assignArg2(&$arg)
    {
        echo "assignArg2:\n";
        $arg = $this->a1;
    }

    public function assignArg3($dummy)
    {
        echo "assignArg3:\n";
        echo spl_object_hash($dummy);
        echo "\n";
        $dummy->d1 = $this->a1;
    }

    public function assignArg4(&$dummy)
    {
        echo "assignArg4:\n";
        echo spl_object_hash($dummy);
        echo "\n";
        $dummy->d1 = $this->a1;
    }

    public function assignArg5($arr)
    {
        echo "assignArg5:\n";
        $arr[0] = -1;
        $arr[] = 10;
    }

    public function assignArg6(&$arr)
    {
        echo "assignArg6:\n";
        $arr[0] = -1;
        $arr[] = 10;
    }

    public function assignArg7($arr)
    {
        echo "assignArg7:\n";
        $arr[0]->d1 = -1;
        $arr[] = 4;
    }
}

echo "va case...\n";
echo 'assign var $i=30';
echo "\n";

$i = 30;
$aaaa = new A;
$aaaa->setA1(50);

echo "variable call by value\n";
$aaaa->assignArg($i);
echo $i;
echo "\n";

echo "variable reference by value\n";
$aaaa->assignArg2($i);
echo $i;
echo "\n";


// object: always call by reference
//
echo "object case...\n";
echo "new object Dummy\n";
$dummy = new Dummy;
$dummy->d1 = 10;
echo spl_object_hash($dummy);
echo "\n";

$aaaa->assignArg3($dummy);
echo $dummy->d1;
echo "\n";

$aaaa->assignArg4($dummy);
echo $dummy->d1;
echo "\n";


echo "int of array case...\n";
$array1 = [1,2,3];

// array: call by value
//
$aaaa->assignArg5($array1);
var_dump($array1);
echo "\n";

// array: call by reference
//
$aaaa->assignArg6($array1);
var_dump($array1);
echo "\n";


echo "object of array case...\n";
$array1 = [new Dummy,new Dummy];
var_dump($array1);

$aaaa->assignArg7($array1);
var_dump($array1);
echo "\n";


