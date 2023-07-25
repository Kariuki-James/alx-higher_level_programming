#!/usr/bin/node
// Displays the status code of a GET request
// The first argument is the URL to request(GET)
const request = require('request');

if (process.argv.length < 3) {
  const usage = `${process.argv[0]} ${process.argv[1]} <URL>`;
  console.log('No URL provided.');
  console.log('Usage: ', usage);
  process.exit(1);
}

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
