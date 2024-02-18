#!/usr/bin/node
<<<<<<< HEAD
console.log(`${process.argv[2]} is ${process.argv[3]}`);
=======
if (process.argv.length == 2)
{
    console.log("undefined is undefined");
}
else if (process.argv.length == 3)
{
    console.log(process.argv[2] + " is undefined");
}
else
{
    console.log(process.argv[2] + " is " + process.argv[3]);
}
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
