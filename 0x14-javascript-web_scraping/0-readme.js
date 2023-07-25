#!/usr/bin/node

const { readFile } = require('fs');

readFile(process.argv[2], 'utf8', (error, content) => {
  console.log(error || content);
});
