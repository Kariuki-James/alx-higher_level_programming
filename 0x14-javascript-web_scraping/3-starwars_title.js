#!/usr/bin/node
// GET data from Star wars API
// Prints the title of the movie with a given movie ID
// The first argument is the movie ID
const request = require('request');

if (process.argv.length < 3) {
  const usage = `${process.argv[0]} ${process.argv[1]} <movie-id>`;
  console.log('No movie-id provided.');
  console.log('Usage: ', usage);
  process.exit(1);
}

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';
request(`${url}/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
