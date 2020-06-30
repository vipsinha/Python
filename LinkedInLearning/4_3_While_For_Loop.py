n = int(input("Enter Number? "))
a = 0
b = [1,2,3,4,5,6,7,8,9,0]

exitCount = 1
sumOfData = 0
enteredData = 0

#while loop counter
while n>0:
    print(a,n,"\n")
    a+=1
    n-=1

#while loop sum
#print("Enter 0 to exit for the first")
while exitCount !=0:
    exitCount = int(input("Enter 0 to exit "))
    enteredData = float(input("Enter data "))
    sumOfData += enteredData
    
print("Total Sum =",sumOfData)

#for loop
for num in b:
    print(num)

for number in range(30, 41):
    print(number)

#sum loop
count = 0    
print("Sum number")
for number in range(0,4):
    count += number
print(count)
    
