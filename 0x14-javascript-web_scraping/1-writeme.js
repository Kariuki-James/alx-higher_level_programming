#!/usr/bin/node
// Writes a string to a file
// The first argument is the file path
// The second argument is the string to write
const fs = require('fs');

if (process.argv.length < 3) {
  console.log('No file-path provided.');
  const usage = `${process.argv[0]} ${process.argv[1]} <file-path>`;
  console.log('Usage: ', usage);
  process.exit(1);
}

const filePath = process.argv[2];
const fileContent = process.argv[3];
fs.writeFile(filePath, fileContent, 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});
