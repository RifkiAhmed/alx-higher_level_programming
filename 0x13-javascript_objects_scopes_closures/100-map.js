#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const myList = list.map((index, value) => index * value);
console.log(myList);