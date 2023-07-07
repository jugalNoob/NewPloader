thislist = ["apple", "banana", "cherry"]
print(thislist)


list1 = ["abc", 34, True, 40, "male"]

print(type(mylist))


thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



#|||||||||||||||||Python Tuples|||||||||||||||

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)



#|||||||||||||||setArrary


  thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

update()

add()
clear()
copy()


#||||||||||||Python Dictionaries|||||||||||||||||||||||

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

x = thisdict["model"]


x = car.keys() #varibale

print(x)

print(thisdict)
print(thisdict["brand"])

#Change Values
thisdict["year"] = 2018
thisdict.update({"year": 2020})

#Add Dictionary Items
thisdict["color"] = "red"
thisdict.pop("model")

for x in thisdict:
  print(x)

  for x in thisdict.values():
   print(x)


  myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


#Python Conditions and If statements||||||||||||||||||||||


# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


  a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


  a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")