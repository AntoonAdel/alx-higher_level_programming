#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  number = number + 1;
  return (theFunction(number));
};
