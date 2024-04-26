#!/usr/bin/node
function factorial (num) {
  if (num === 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

const int = process.argv[2];
if (isNaN(int)) {
  console.log('1');
} else {
  console.log(factorial(int));
}
