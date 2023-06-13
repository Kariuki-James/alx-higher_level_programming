#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h && parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
