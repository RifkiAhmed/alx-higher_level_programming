#!/usr/bin/node

function secondMax (array) {
  const myArray = [];
  let max1, max2;
  array.forEach((item) => {
    myArray.push(parseInt(item));
  });
  if (myArray.length === 2) {
    max2 = (myArray[0] > myArray[1] ? myArray[1] : myArray[0]);
  } else {
    max1 = max2 = myArray[0];
    myArray.forEach((item) => {
      if (max1 < item) {
        max2 = max1;
        max1 = item;
      } else if (max2 < item) {
        max2 = item;
      }
    });
  }
  return max2;
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondMax(process.argv.slice(2)));
}
