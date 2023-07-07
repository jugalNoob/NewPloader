<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>jugal sharma</h1>
    <script>
          const letters = new Set(["a","b","c"]);
          letters.add("kanika")
          letters.add({"email":"jugal@gmail.com"})
console.log(letters)
console.warn(letters.has("a"))
console.log(letters.size)
//data.clear()
letters.delete("a")
for(x of letters){
    console.log(x)
}

console.log(letters.keys())

console.log(letters.values())

console.log(letters.entries())

    </script>
    
</body>
</html>