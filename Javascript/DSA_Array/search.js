
  let data=[10 , 20 , 30 , 40 , 50];

  let temp=20;

  let ko=undefined;

  for(let i=0; i<data.length; i++){

    if(temp== data[i]){

      ko=i
      //ko=data[i]
    }
  }

console.log(ko)

  return (
    <div>
      <h1>linear search</h1>
    </div>
  )
}

export default Search