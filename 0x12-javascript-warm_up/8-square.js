#!/usr/bin/node
const square = parseInt(process.argv[2]);
let size = 0;
if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (size = 0; size < square; size++) {
    console.log('X'.repeat(square));
  }
}
