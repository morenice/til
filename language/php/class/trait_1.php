<?php

class Hello
{
	public function sayHello() {
		echo "Hello\n";
	}
}

class HelloWorldPhp extends Hello
{
	use Meet;
	public function sayHello() {
		echo "Hello world\n";
	}
}

trait Meet
{
	public function requestMeet() {
		echo "I want to metting.\n";
	}
}

$helloWorld = new HelloWorldPhp();
$helloWorld->sayHello();
$helloWorld->requestMeet();
