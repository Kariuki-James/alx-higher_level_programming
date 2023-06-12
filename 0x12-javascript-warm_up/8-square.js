#!/usr/bin/node
const sizeOfSquare = parseInt(process.argv[2]);
if (!sizeOfSquare) {
  console.log('Missing size');
  process.exit();
}

for (let row = 0; row < sizeOfSquare; row++) {
  for (let col = 0; col < sizeOfSquare; col++) {
    process.stdout.write('X');
  }
  process.stdout.write('\n');
}
