#!/usr/bin/node
function add(a, b)
{
    let num = a + b;
    console.log(num);
}
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
add(a, b);