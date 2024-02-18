#!/usr/bin/node
<<<<<<< HEAD
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
=======
let num = parseInt(process.argv[2]);
if (isNaN(num))
{
    console.log('Not a number');
}
else
{
    console.log('My number: ' + num);
}
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
