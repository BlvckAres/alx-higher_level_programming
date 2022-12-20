#!/usr/bin/bash/node
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : 'My number: ${num}');