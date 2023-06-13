#!/usr/bin/node
const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
      return;
    }

    for (let h = 0; h < this.height; h++) {
      for (let w = 0; w < this.width; w++) {
        process.stdout.write(`${c}`);
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;
