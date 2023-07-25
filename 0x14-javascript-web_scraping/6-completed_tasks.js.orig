#!/usr/bin/node
// Computes the number of tasks completed by user id
// The first argument is the API url
// Prints only users with completed tasks.
const request = require('request');

if (process.argv.length < 3) {
  const usage = `${process.argv[0]} ${process.argv[1]} <api-url>`;
  console.log('Missing API url');
  console.log('Usage: ', usage);
  process.exit(1);
}

const url = process.argv[2];
const filter = '?completed=true';

request(url + filter, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const completedTasks = JSON.parse(body);
    const users = {};
    for (const task of completedTasks) {
      const userId = task.userId;
      if (users[userId]) {
        users[userId] += 1;
      } else {
        users[userId] = 1;
      }
    }
    console.log(users);
  }
});
