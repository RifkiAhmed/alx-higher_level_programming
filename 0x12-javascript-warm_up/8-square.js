#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let i, j, str;
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    str = '';
    for (j = 0; j < parseInt(process.argv[2]); j++) {
      str += 'X';
    }
    console.log(str);
  }
}
