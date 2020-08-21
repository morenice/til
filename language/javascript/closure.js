'use strict'

function closure(val) {
  let tmp = 'tmp';
  function __closure(){
    console.log(tmp)
    console.log(val)
  }
  return __closure;
}

let c1 = closure(4);
c1();
let c2 = closure(10);
c2();
