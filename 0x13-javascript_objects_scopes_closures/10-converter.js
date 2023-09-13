#!/usr/bin/node

exports.converter = function (base) {
  function toBase (number) {
    if (number > 0) {
      if (base === 16 && number > 9 && number <= 15) {
        const hexdecimal = ['a', 'b', 'c', 'd', 'e', 'f'];
        return toBase(Math.floor(number / base)) + '' + hexdecimal[number - 10];
      } else {
        return toBase(Math.floor(number / base)) + '' + number % base;
      }
    } else {
      return '';
    }
  }
  return function (number) {
    return toBase(number);
  };
};
