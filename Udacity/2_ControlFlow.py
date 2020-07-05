# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 232 #provide answer
guess = 157 #provide guess

if answer > guess :#provide conditional
    result = "Oops!  Your guess was too low."
elif answer < guess: #provide conditional
    result = "Oops!  Your guess was too high."
elif answer == guess: #provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)

# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'CA'#Either CA, MN, or NY
purchase_amount = 1500#amount of purchase

if state == 'CA':#provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif 'MN':#provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif 'NY':#provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

'''
Practice: Quick Brown Fox
Use a for loop to take a list and print each element of the list in its own line.
'''
# Note: Range is used when we need index
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)

'''
Practice: Multiples of 5
Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
'''
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for num in range(5,31,5):
    print(num)

'''
Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
'''
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for index in range(len(names)):
    # don't forgot .append to add into the list
    usernames.append(names[index].lower())
    usernames[index] = usernames[index].replace(" ", "_")

print(usernames)

#####Another way
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ", "_")

print(usernames)

'''
Quiz: Tag Counter
Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings.
'''
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for string in tokens:
    if string[0] == '<' and string[-1] == '>':
        count +=1

print(count)

'''
Quiz: Create an HTML List
Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

<ul>
<li>first string</li>
<li>second string</li>
</ul>
'''
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>"
    html_str += item
    html_str += "</li>\n"
html_str += "</ul>"

print(html_str)

'''
When you iterate through a dictionary using a for loop, doing it the normal way 
(for n in some_dict) will only give you access to the keys in the dictionary - 
which is what you'd want in some situations. In other cases, you'd want to iterate 
through both the keys and values in the dictionary. Let's see how this is done 
in an example. Consider this dictionary that uses names of actors as keys 
and their characters as values.
'''
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key,values in basket_items.items():
    #if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        result += values

print(result)

'''
Sum all odd number in list
'''

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))

'''
Quiz: Break the String
Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.
'''
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
char_in_ticker = 0
# write your loop here
for statement in headlines:
    if char_in_ticker+len(statement) < 140:
        news_ticker += statement
        news_ticker += " "
        char_in_ticker = len(news_ticker)
    elif char_in_ticker != 140:
        for char in statement:
            while(char_in_ticker < 140):
                news_ticker += char
                char_in_ticker +=1
                break
    else:
        break

print(news_ticker)

#Another solution
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

'''
Quiz: Zip Coordinates
Use zip to write a for loop that creates a string specifying the label 
and coordinates of each point and appends it to the list points. Each 
string should be formatted as label: x, y, z. For example, the string 
for the first coordinate should be F: 23, 677, 4.
'''
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

'''
Quiz: Unzip Tuples
Unzip the cast tuple into two names and heights tuples.
'''
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)

'''
Enumerate
enumerate is a built in function that returns an iterator of tuples 
containing indices and values of a list. You'll often use this when 
you want the index along with each element of an iterable in a loop.
'''
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)