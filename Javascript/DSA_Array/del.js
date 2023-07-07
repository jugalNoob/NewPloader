import React,{useState} from 'react'

function Del() {




  const [del , setDel]=useState()


  function func(e){
    e.preventDefault();
    let data=[10 , 20 , 30 , 40 , 50 ,60];
        // let posti=document.getElementById("posti").value;
        let posti=del;
        posti=parseInt(posti)
        for(let i=posti; i<data.length-1; i++){  
          data[i]=data[i+1];
        }
        data.length=data.length-1;
        console.log(data)
    }
    



  return (
    <div>
    <h1>delete algo</h1>


<input type="text" name="" value={del} id="" onChange={(e)=>setDel(e.target.value)} />

<button onClick={func}>clic</button>

{/* <input type="number" name="number"  id="pistion" />
{/* <input type="text"  value={del} name="del" id="" onChange={(e)=>setDel(e.target.value)}/> */}

{/* <button onClick={Changes}>click</button> */} 


      
    </div>
  )
}

export default Del