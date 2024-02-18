#!/usr/bin/node
<<<<<<< HEAD
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
=======
if (process.argv[2] == null)
{
    console.log('No argument');
}
else
{
    console.log(process.argv[2]);
}
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
