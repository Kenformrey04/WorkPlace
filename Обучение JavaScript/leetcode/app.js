"use strict";
let nums =  [3,1,2,10,1];

function sum(arr) {
    let number = 0;
    for (let i = 1; i < arr.length; i++) {
        arr[i] += arr[i-1];
    }
    return arr;
}

console.log(sum(nums));





