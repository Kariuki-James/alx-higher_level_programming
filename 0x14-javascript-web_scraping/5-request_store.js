#!/usr/bin/node
// GET contents of a webpage and store in a file
// The first argument is the url to request
// The second argument is the file path to store content.
const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  const usage = `${process.argv[0]} ${process.argv[1]} <url> <file-path>`;
  console.log('Missing arguments');
  console.log('Usage: ', usage);
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
