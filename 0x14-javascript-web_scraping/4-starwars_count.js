#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (body) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      for (const j in films[i].characters) {
        if (films[i].characters[j].endsWith('/18/')) { count++; }
      }
    }
    console.log(count);
  }
});
