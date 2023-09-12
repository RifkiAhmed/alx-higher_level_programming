#!/usr/bin/node

function secondMax (array) {
  let max1, max2;
  max1 = max2 = parseInt(array[0]);
  array.forEach((item) => {
    item = parseInt(item);
    if (max1 < item) {
      max2 = max1;
      max1 = item;
    } else if (max2 < item) {
      max2 = item;
    }
  });
  return max2;
}
if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondMax(process.argv.slice(2)));
}
