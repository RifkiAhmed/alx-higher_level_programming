#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (body) {
    body = JSON.parse(body);
    const dict = {};
    body.forEach((todo) => {
      if (todo.completed === true) {
        if (dict[todo.userId] === undefined) {
          dict[todo.userId] = 1;
        } else {
          dict[todo.userId]++;
        }
      }
    });
    console.log(dict);
  }
});
