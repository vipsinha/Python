# Loop 1
print('####Loop_1#####')

nums = [1,2,3,4,5]
for num in nums:
    print(num)

# Loop 2
print('####Loop_2#####')

nums = [1,2,3,4,5]
for num in nums:
    if(num == 2):
        print('Found 2')
        break # break out of for loop
    print(num)

# Loop 3
print('####Loop_3#####')

nums = [1,2,3,4,5]
for num in nums:
    if(num == 2):
        print('Found 2')
        break
print(num)

# Loop 4
print('####Loop_4#####')

nums = [1,2,3,4,5]
for num in nums:
    if(num == 2):
        print('Found 2')
        continue
    print(num)

# Loop 5
print('####Loop_5#####')

nums = [1,2,3,4,5]
for num in nums:
    if(num == 2):
        print('Found 2')
        continue
print(num)

# Loop 6
print('####Loop_6#####')

nums = [1,2,3]
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Loop 7
print('####Loop_7#####')

nums = [1,2,3]
for num in range(10):
    print(num)

# Loop 8
print('####Loop_8#####')

for num in range(1,11):
    print(num)

# Loop 9
print('####Loop_9#####')

x = 0
while x < 10:
    x +=1
    print(x)

# Loop 10
print('####Loop_10#####')

x = 0
while x < 10:
    if(x == 5):
        break # break out from every where
    x +=1
    print(x)

# Loop 11
print('####Loop_11#####')

x = 0
while True:
    if(x == 5):
        break # break out from every where
    x +=1
    print(x)
