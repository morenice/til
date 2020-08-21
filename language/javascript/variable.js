'use strict'

function printGlobalVariable() {
  console.log(globalVar1);
  console.log(globalVar2);
}

function localVariable() {
  // block variable
  let localVar1 = 1;
  let localVar2 = 2;
}

function constVariable() {
  // const block variable
  const constVar1 = 10;
  const constVar2 = "timestamp";

  try {
    constVar2 = 30;
  } catch (e) {
    console.log(e);
  }
}


function nullOrUndefined() {
  let a;
  console.log("a = " + a); // undefined(not assigned)

  a = null;
  console.log("a = " + a); // null

  var n = null;
  console.log(n * 32); // used 0 or false
}


function variableHoisting() {
  console.log(novar);

  let novar = 1;

}


var globalVar1 = 1;
var globalVar2 = 2;

printGlobalVariable();
console.log(globalVar1);
console.log(globalVar2);

localVariable();
try {
  console.log(localVar1);
  console.log(localVar2);
} catch (e) {
  console.log(e);
}

constVariable();
nullOrUndefined();
