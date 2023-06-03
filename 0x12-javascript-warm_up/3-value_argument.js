#!/usr/bin/node
let myStr;

if (process.argv.length < 3) {
  myStr = 'No argument';
} else {
  myStr = process.argv[2];
}
console.log(myStr);
