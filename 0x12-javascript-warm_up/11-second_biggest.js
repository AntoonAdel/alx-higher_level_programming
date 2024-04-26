#!/usr/bin/node
const argvNums = process.argv;

function secondBiggest (array) {
  if (array.length <= 3) {
    return (0);
  }
  array = array.slice(2).map(num => parseInt(num));

  const maxNum = Math.max(...array);
  const arrFilter = array.filter(arrFilter => arrFilter < maxNum);

  return (Math.max(...arrFilter));
}
console.log(secondBiggest(argvNums));
