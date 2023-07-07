import { ethers } from "ethers";
import abi from "./ABI.json"

console.log("jugal")


const polygon=new Promise((res,rej)=>{

    async function meta(){
        const contractAddress="0xA5AF6627780Cbd328337043AE1037D650B4e32Ea";


const provider = new ethers.providers.Web3Provider(window.ethereum)
const account=await provider.send("eth_requestAccounts", []);
const signer=provider.getSigner()
const address = await signer.getAddress()


const contract=new ethers.Contract(contractAddress, abi , provider)

const tatales=await contract.totalSupply();

console.log(tatales.toString())

//Balances

const totalsupply=await contract.totalSupply().call({
    from:account[0]
});

console.log(totalsupply)

const maxsupply=await contract.maxSupply().call({from:account[0]})

console.log(maxsupply)


let objects=await contract.getOwnerObjects().call({from:account[0]})

console.log(objects)




    }
    meta()
})