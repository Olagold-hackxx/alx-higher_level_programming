#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (response) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const result of results) {
      for (const characters of result.characters) {
        if (characters.includes('18')) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
