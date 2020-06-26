package main

import (
	"fmt"
	"strings"
	"github.com/morenice/tutorial/some_package"
)

func add(a int, b int) int {
	return a * b
}

func getFirstAndLastChar(s string) (string, string) {
	// return variable case #1
	//
	splitedString := strings.Split(s, "")
	return splitedString[0], splitedString[len(splitedString)-1]
}

func getFirstAndLastChar2(s string) (first string, last string) {
	// return variable case #2
	//
	splitedString := strings.Split(s, "")
	first = splitedString[0]
	last = splitedString[len(splitedString)-1]

	// only write return keyword
	return
}

func getFirstAndLastChar3(s string) (first string, last string) {
	// return variable case #3
	//
	// defer keyword: Useful File/Socket close
	defer fmt.Println("Run after to finish this function")
	defer fmt.Println("Run2 after to finish this function")

	splitedString := strings.Split(s, "")
	first = splitedString[0]
	last = splitedString[len(splitedString)-1]

	// only write return keyword
	return
}

func printAllParams(s ...string) {
	// s: string type list
	fmt.Println(s)
}

func main() {
	fmt.Println("Hello Golang")
	some_package.Public_access_function()

	// constant and variable
	const name = "greg"
	var name2 string = "greg2"
	name2 = "flynn"
	fmt.Println(name)
	fmt.Println(name2)

	// skip type of var :=
	fullName := "Gregory"
	var fullName2 string = "Gregory"
	fmt.Println(fullName)
	fmt.Println(fullName2)

	// Call function
	fmt.Println(add(5, 6))
	fmt.Println(getFirstAndLastChar("Good test"))
	fmt.Println(getFirstAndLastChar2("Good test"))
	fmt.Println(getFirstAndLastChar3("Good test"))
	printAllParams("1234", "456", "78a")
}