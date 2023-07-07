import React,{useState,useEffect} from 'react'
import sha256 from 'crypto-js/sha256';


function App() {

  const [email, setEmail]=useState()
  const [password , setPassword]=useState()
const [cpassword , setCpassword]=useState()

const ChangePassword=()=>{
  
  const hashss = sha256( password);
  const hashtwo=sha256(cpassword)


  if(!password || !cpassword){
    alert("chedck password")
  }else{
  const pushed=[]
  pushed.push(hashss.toString() , hashtwo.toString())
  for(let i=0; i<pushed.length; i++){
    // console.log(pushed[i])
    for(let j=i+1; j<pushed.length; j++){
      if(pushed[i] === pushed[j]){
        console.log(true , "jugal")          
        return true
      }
    }
console.log(false)
  }
  }
  // console.log(pushed)
  ///last row class line
}




const [passwordTwo , setPasswordTwo]=useState()

const ChangePasswordTwo=()=>{
  const hash = sha256(passwordTwo);
  console.log(hash.toString());
}

// console.log(password === passwordTwo)


  return (
    <div>
 <br />
    <input type="text" name="" id=""  onChange={(e)=>setPassword(e.target.value)} placeholder='enter password all'/>
<br />
<input type="text" name="" id="" placeholder='cpassword' onChange={(e)=>setCpassword(e.target.value)}/>
    <br />
    <button onClick={ChangePassword}>Click </button>

    <br />
    <br />
    <input type="text" name="" id="" onChange={(e)=>setPasswordTwo(e.target.value)}  placeholder='enter password Two'/>
    <br />
    <button onClick={ChangePasswordTwo}>second</button>
    </div>
  )
}

export default App