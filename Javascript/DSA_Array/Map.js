<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <input type="text"  name="" id="posti">
    <button onclick="func()">clic</button>

    <script>
        function func(){

 
let data=[10 , 20 , 30 , 40 , 50 ,60];
    let posti=document.getElementById("posti").value;

    posti=parseInt(posti)
    for(let i=posti; i<data.length-1; i++){  
      data[i]=data[i+1];
    }
    data.length=data.length-1;
    console.log(data)
}

        //MAP
        //Map use key and value

//    let data=new Map([
//     ["name" , "jugal"],
//     [true , "book key"],
//     [100 , "hynder"]
//    ]);
//    data.set("color" , "blue")

//    console.log(data)
//    console.warn(data.size)
//    console.log(data.has(100))
//    console.log(data.get(100))
   //data.clear()
    </script>
</body>
</html>