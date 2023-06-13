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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = parseInt(this.width) * 2;
    this.height = parseInt(this.height) * 2;
  }
}

module.exports = Rectangle;
