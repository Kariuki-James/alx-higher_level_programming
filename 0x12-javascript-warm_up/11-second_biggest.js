#!/usr/bin/node
if (!process.argv[3]) {
  console.log(0);
  process.exit();
}
const splicedArray = process.argv.splice(2);

let largest = parseInt(splicedArray[0]);
let secLargest = null;
for (let num of splicedArray) {
  num = parseInt(num);
  if (num === largest) {
    continue;
  }
  if (num > largest) {
    secLargest = largest;
    largest = num;
  }
  if (num > secLargest && num < largest) {
    secLargest = num;
  }
  if (num < 0 && secLargest === null) {
    secLargest = num;
  }
}
if (secLargest === null) {
  secLargest = 0;
}
console.log(secLargest);
