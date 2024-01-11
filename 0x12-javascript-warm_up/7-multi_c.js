#!/usr/bin/node
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