#!/usr/bin/node
<<<<<<< HEAD
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < size; r++) {
    let row = '';
    for (let c = 0; c < size; c++) row += 'X';
    console.log(row);
  }
}
=======
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
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
