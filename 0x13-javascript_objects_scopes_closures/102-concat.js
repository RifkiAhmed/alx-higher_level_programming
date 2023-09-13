#!/usr/bin/node
const fileSystem = require('fs');

fileSystem.readFile(process.argv[2], (error, buffer1) => {
  if (error) {
    console.erroror(error.message);
    process.exit(1);
  }

  fileSystem.readFile(process.argv[3], (error, buffer2) => {
    if (error) {
      console.erroror(error.message);
      process.exit(1);
    }

    fileSystem.writeFile(process.argv[4], buffer1 + buffer2 + '\n', (error) => {
      if (error) {
        console.erroror(error.message);
        process.exit(1);
      }
    });
  });
});
