#!/usr/bin/node

exports.esrever = function (list) {
  let i = 1;
  const myList = [];
  while (i <= list.length) {
    myList.push(list[list.length - i]);
    i++;
  }
  return myList;
};
