#!/usr/bin/bash/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
    console.log('Missing number of occurrences');}
else {
    for (let y = 0; y < x; y++) {
        console.log("C is fun");
    }
}
