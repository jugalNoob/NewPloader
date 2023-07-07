import React,{useState , useEffect} from 'react'
import { NavLink } from 'react-router-dom'
import { ethers } from "ethers";
import abi from "./ABI.json"
import Meta from './Meta';
function Home() {

  
  const [state , setState]=useState({
    provider:null,
    signer:null,
    contract:null
})

const contractAddress="0xe0BABA4c7c48E0eF687Dc33EaE37b8bC9dbF5419";

const [Addresss, setAddresss]=useState();

useEffect(()=>{
  const Checker=async()=>{
    const provider = new ethers.providers.Web3Provider(window.ethereum)
    const account=await provider.send("eth_requestAccounts", []);
    const signer=provider.getSigner()
    const address = await signer.getAddress()
   
    const contract=new ethers.Contract(contractAddress ,  abi , signer)

    setAddresss(address)

    setState({provider , signer , address , contract})   


  }

  Checker()
},[])




const [bal , setBal]=useState()
useEffect(()=>{
const All=async()=>{
const {provider ,  address}=state;
const balance=await provider.getBalance(address)
const balaether=ethers.utils.formatEther(balance, "ether")

// console.log(balaether)
setBal(balaether)
}
All()

},[state])
  return (
    <div>
    <h1>{Addresss}</h1>

    <br />
    <h1>{bal}</h1>

        <NavLink to="/">Home</NavLink>
        <br />
        <NavLink to="/meta">Metaverse</NavLink>
        <br />

<Meta state={state}></Meta>


    </div>
  )
}

export default Home