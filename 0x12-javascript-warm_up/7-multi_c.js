#!/usr/bin/node
<<<<<<< HEAD
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
=======
if (process.argv.length == 2)
{
    console.log('Missing number of occurrences');
}
let num = parseInt(process.argv[2]);
if (!isNaN(num))
{
    for (let x = 0; x < num; x++)
    {
        console.log('C is fun');
    }
}
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
