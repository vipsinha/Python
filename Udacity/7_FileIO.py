fr = open('./7_FileIn.txt', 'r')
filestring = fr.read()
fr.close()

print(filestring)

fw = open('./7_FileOut.txt', 'w')
fw.write(filestring)
fw.close()

'''
With
Python provides a special syntax that auto-closes a file for you once you're finished using it.

This with keyword allows you to open a file, do operations on it, 
and automatically close it after the indented code is executed, in this case, 
reading from the file. Now, we don’t have to call f.close()! You can only access 
the file object, f, within this indented block.
'''
with open('./7_FileIn.txt', 'r') as f:
    file_data = f.read()

print(file_data)

with open("7_FileIn.txt") as song:
    print(song.read(10))
    print(song.read(20))
    print(song.read())

'''
if wish to read line by line
'''
with open("7_FileIn.txt") as song:
    print(song.readline())


'''
To strip '\n'
'''
camelot_lines = []
with open("7_FileIn.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)


'''
Quiz: Flying Circus Cast List
You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

Write a function called create_cast_list that takes a filename as input 
and returns a list of actors' names. It will be run on the file flying_circus_cast.txt 
(this information was collected from imdb.com). Each line of that file consists of an actor's name, 
a comma, and then some (messy) information about roles they played in the programme. 
You'll need to extract only the name and add it to a list. You might use the .split() method to process each line.
'''
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename, 'r') as data:
        for cast in data:
            cast_list.append(cast.split(",")[0])
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

'''
Question: Create a function that opens the flowers.txt, 
reads every line in it, and saves it as a dictionary. 
The main (separate) function should take user input 
(user's first name and last name) and parse the user input 
to identify the first letter of the first name. It should 
then use it to print the flower name with the same 
first letter (from dictionary created in the first function).
'''
# Write your code here

# HINT: create a dictionary from flowers.txt
f_keys = []
f_values = []
f_dict = {}
with open('flowers.txt','r') as flowerfile:
    for flower in flowerfile:
        f_keys.append(flower.split(':')[0])
        f_values.append(flower.split(' ')[1])
f_dict = dict(zip(f_keys,f_values))

# HINT: create a function to ask for user's first and last name
def get_username():
    name = str(input("Enter full name:").upper())
    for keys,values in f_dict.items():
        if name[0] == keys:
            return(values)
        #return(name[0])

# print the desired output
print(get_username())