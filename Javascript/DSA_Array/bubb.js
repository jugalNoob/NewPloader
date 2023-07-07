

let data=[8 , 6 , 7 , 5 , 3 , 2 , 1]

console.log(data)

for(let i=0; i<data.length; i++){

  for(let j=0; j<data.length; j++){

    if(data[j] > data[j+1]){

      let temp=data[j]

      data[j]=data[j+1]

      data[j+1]=temp
    }
  }
}
console.log(data)