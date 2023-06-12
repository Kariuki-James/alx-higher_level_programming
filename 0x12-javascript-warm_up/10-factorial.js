#!/usr/bin/node
function factorial (a) {
  const num = parseInt(a);
  if (num && num > 0) {
    return (num * factorial(num - 1));
  }
  return (1);
}
console.log(factorial(process.argv[2]));
