#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (body) {
    const todos = JSON.parse(body);
    const dict = {};
    for (let i = 1; i <= 10; i++) {
      let count = 0;
      todos.forEach((todo) => {
        if (todo.userId === i) {
          if (todo.completed) {
            count++;
          }
        }
      });
      dict[i] = count;
    }
    console.log(dict);
  }
});
