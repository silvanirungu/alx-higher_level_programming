#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num))
{
    console.log('Missing size');
}
for (let x = 0; x < num; x++)
{
    for (let y = 0; y < num; y++)
    {
        process.stdout.write('X');
    }
    console.log();
}