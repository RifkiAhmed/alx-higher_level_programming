#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api';
request(url + '/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (body) {
    const film = JSON.parse(body);
    const characters = film.characters;
    characters.forEach((character) => {
      request(character, (error, response, body) => {
        if (error) {
          console.error(error);
        }
        body = JSON.parse(body);
        console.log(body.name);
      });
    });
  }
});
