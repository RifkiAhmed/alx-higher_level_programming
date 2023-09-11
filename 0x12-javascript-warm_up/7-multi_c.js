#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
