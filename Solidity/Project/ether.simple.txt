import React, { useEffect } from 'react';
import * as THREE from 'three';
import { ethers } from 'ethers';
import abi from './ABI.json';

function Meta() {
  useEffect(() => {
    const initMetaverse = async () => {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contractAddress = '0x8Cb1A066B5C8d88F8aE8b9f121cD538A5b1318f6'; // the contract address
      const contract = new ethers.Contract(contractAddress, abi, signer);
      // const objectName = 'My Object';
      // const w = 20;
      // const h = 1;
      // const d = 10;
      // const x = 5;
      // const y = 3;
      // const z = 1;
      // const overrides = {
      //   value: ethers.utils.parseEther('0.1'), // the cost of minting
      // };
      // await contract.mint(objectName, w, h, d, x, y, z, overrides);
      const ownedNFTs = await contract.getOwnerObjects();
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      camera.position.z = 5;
      const renderer = new THREE.WebGLRenderer();
      renderer.setSize(window.innerWidth, window.innerHeight);
      document.body.appendChild(renderer.domElement);
      for (let i = 0; i < ownedNFTs.length; i++) {

        console.log(ownedNFTs)
        const nftInfo = ownedNFTs[i];
        const geometry = new THREE.BoxGeometry(nftInfo.w, nftInfo.h, nftInfo.d);
        const material = new THREE.MeshBasicMaterial({ color: 0x008200 });
        const nft = new THREE.Mesh(geometry, material);
        scene.add(nft);
        nft.position.set(nftInfo.x, nftInfo.y, nftInfo.z);
      }
      const animate = () => {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
      };
      animate();
    };
    initMetaverse();
  }, []);

  return <div>Meta metaverse</div>;
}

export default Meta;
