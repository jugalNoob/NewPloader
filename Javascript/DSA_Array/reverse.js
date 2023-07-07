const array = [1, 2, 3, 4]

const reversedArray = []

for(let i = array.length - 1; i >= 0; i--) {
  const valueAtIndex = array[i]
  
  reversedArray.push(valueAtIndex)
}

console.log(reversedArray)
// [4, 3, 2, 1]


arr = [1, 2, 3, 4];
arr1 = [];
for (let i = arr.length - 1; i >= 0; i--) {
    arr1.push(arr[i]);
}
console.log(arr1);




let data = [5, 12, 65, 89, 0,100,200];
let temp;
function customReverse(data,start,end) {
  console.warn(data)
  if (start <= end) {
    temp = data[start];
    data[start] = data[end];
    data[end] = temp;
    customReverse(data, start + 1, end - 1);
  }
}

customReverse(data, 0, data.length - 1);