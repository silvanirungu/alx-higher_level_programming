#!/usr/bin/node
<<<<<<< HEAD
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
=======
if (process.argv.length == 2)
{
    console.log("No argument");
}
else if (process.argv.length == 3)
{
    console.log("Argument found");
}
else
{
    console.log("Arguments found");
}
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
