#!/usr/bin/node
<<<<<<< HEAD
function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
=======
function add(a, b)
{
    let num = a + b;
    console.log(num);
}
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
add(a, b);
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
