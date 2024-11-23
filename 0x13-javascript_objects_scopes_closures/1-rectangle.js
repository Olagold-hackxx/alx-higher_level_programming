#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }

  area() {
    return this.width * this.height;
  }
}
module.exports = Rectangle;
