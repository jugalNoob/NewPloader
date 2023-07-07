import React from 'react'

function Inst() {

    let data=[10 , 20 , 30 , 40]

    let newel=70;

    let posti=0;

    for(let i=data.length-1; i>=0 ; i--){

        console.log(data[i])

        if(i>=posti){
            data[i+1]=data[i]
            if(i==posti){
                data[i]=newel
            }
        }
    }
    console.log(data)
  return (
    <div>
      <h1>Insert string element</h1>

      
    </div>
  )
}

export default Inst



// function insertEl() {
//   let data = [60, 30, 10, 67, 40];
//   let newEl = document.getElementById('newEl').value;
//   newEl = parseInt(newEl)
//   let position = document.getElementById('position').value
//   console.warn(data);

//   for (let i = data.length - 1; i >= 0; i--) {
//     // console.warn(data[i])
//     if (i >= position) {
//       data[i + 1] = data[i];
//       if (i == position) {
//         data[i] = newEl;
//       }
//     }
//   }
//   console.warn(data)
// }