
// JavaScript   find   min values using loop and array  show all code
// Find max value
let arr = [1, 2, 3, 4, 5];
let max = [0]

for (let i = 0; i < arr.length; i++) {
if (arr[i] > max) {
max = arr[i];
}
}

console.log(max); // 5

///Find  Mini number

let numbers = [15, 10, 15, 20, 25];
let min = numbers[0];

for (let i = 0; i < numbers.length; i++) {
if (numbers[i] < min) {
min = numbers[i];
}
}

console.log(min); // Output: 5



//JavaScript   find max and min values using loop and array full code?


// const numbers = [4, 60, 53, 26, 2]

// let maximum = -Infinity
// let minimum = Infinity

// for(let number of numbers){
//     if(number > maximum)
//         maximum = number
        
//     if(number < minimum)
//         minimum = number
//  }
 
// console.log(`Maximum Value: ${getMaxOfArray(numbers)}` + `\nMinimum Value: ${getMinOfArray(numbers)}`);