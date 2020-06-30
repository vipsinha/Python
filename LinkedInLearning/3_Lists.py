names1 = []
names2 = ["Vipul", "Summer", "July"]
ages2 = [22,12,32,11]
myList = [0,1,2,3,4,5,6,7,8,9]

print("***Print multiple list***")
print(names2,ages2,myList)

print("***Fwd Index***")
print(names2[0])
print(names2[1])
print(names2[2])

print("***Bkwd Index***")
print(names2[-3])
print(names2[-2])
print(names2[-1])

print("***Append a new data***")
names2.append("Append")

print(names2)

print("***Add list into other list***")
names2.extend(ages2)
print(names2)

print("***Remove data***")
names2.remove("Summer")
print(names2)

print("***Print list length***")
print(len(names2))

print("***Print list max element***")
print(max(ages2))

#[x:y]-- x=start element, y=end element index+1
print("***print from 4th index***")
print(myList[4:8])
print(myList[2:7])
print(myList[2:3])
print(myList[2:2])

print("*** print element from start***")
print(myList[:10])
print("***print element at end***")
print(myList[-1:])
print("***print element at middle***")
print(myList[-4:-2])
print("***print element at middle***")
print(myList[-6:])
print("***print all element***")
print(myList[:])
print("***print elements with gaps***")
print(myList[0:10:2])
print(myList[0:10:3])
print(myList[::4])
print(myList[::-2])

