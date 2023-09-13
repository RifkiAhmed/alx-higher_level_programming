#!/usr/bin/node
const data = require('./101-data').dict;
const sorted = {};
for (const item in data) {
  if (!sorted[data[item]]) {
    sorted[data[item]] = [];
  }
  sorted[data[item]].push(item);
}
console.log(sorted);
