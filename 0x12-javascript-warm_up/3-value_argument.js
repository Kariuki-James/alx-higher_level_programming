#!/usr/bin/node
if (process.argv[2]) {
  const slicedArray = process.argv.slice(2);
  console.log(slicedArray.join(' '));
} else {
  console.log('No argument');
}
