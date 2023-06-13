#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h && parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      for (let w = 0; w < this.width; w++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Rectangle;
