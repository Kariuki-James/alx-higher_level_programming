#!/usr/bin/node
// GET data from Star wars API
// Prints the number of the movies where the character
// "Wedge Antilles" is present. (character id - 18)
// The first argument is the endpoint url.
const request = require('request');

if (process.argv.length < 3) {
  const usage = `${process.argv[0]} ${process.argv[1]} <api-url>`;
  console.log('No api-url provided.');
  console.log('Usage: ', usage);
  process.exit(1);
}

const url = process.argv[2];
const hasCharId = (url) => {
  return url.includes('18');
};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    const filtered = movies.filter((movie) =>
      movie.characters.some((url) => hasCharId(url))
    );
    console.log(filtered.length);
  }
});
