#!/usr/bin/env node
const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg1 === undefined || arg2 === undefined) {
  console.log('No argument');
} else {
  console.log(`${arg1} is ${arg2}`);
}