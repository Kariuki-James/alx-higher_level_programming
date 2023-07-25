#!/usr/bin/node
// Reads and prints contents of a file passed as first argument
const fs = require('fs');

if (process.argv.length < 3) {
  console.log('No file-path provided.');
  const usage = `${process.argv[0]} ${process.argv[1]} <file-path>`;
  console.log('Usage: ', usage);
  process.exit(1);
}

const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
