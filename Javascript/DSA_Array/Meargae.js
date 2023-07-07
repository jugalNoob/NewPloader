import React from 'react'

function Merge() {

    let data=[10 , 20 , 30 , 40]

    let data2=[50 , 60 , 70 , 80]
    let data3=[];

  //  console.log(data.concat(data2))

    for(let i=0; i<data.length; i++){
        data3[i]=data[i]
    }

    for(let i=0; i<data2.length; i++){
        data3[data.length+i]=data2[i]
    }

    console.log(data3)
  return (
    <div>
      <h1>merge</h1>
    </div>
  )
}

export default Merge