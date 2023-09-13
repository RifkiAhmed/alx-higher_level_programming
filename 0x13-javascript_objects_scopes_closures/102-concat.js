#!/usr/bin/node
const fileSystem = require('fs');

fileSystem.readFile(process.argv[2], (error, buffer1) => {
  if (error) {
    console.log(error);
  }

  fileSystem.readFile(process.argv[3], (error, buffer2) => {
    if (error) {
      console.log(error);
    }

    fileSystem.writeFile(process.argv[4], buffer1 + buffer2, (error) => {
      if (error) {
        console.log(error);
      }
    });
  });
});
