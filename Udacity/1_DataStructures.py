'''
A good understanding of data structures is integral for programming and data analysis. 
As a data analyst, you will be working with data and code all the time, so a solid understanding 
of what data types and data structures are available and when to use each one will help you write more efficient code.

Remember, you can get more practice on sites like HackerRank.

In this lesson, we covered four important data structures in Python:

Data Structure	    Ordered	        Mutable	    Constructor	        Example
List	            Yes	            Yes	        [ ] or list()	    [5.7, 4, 'yes', 5.7]
Tuple	            Yes	            No	        ( ) or tuple()	    (5.7, 4, 'yes', 5.7)
Set	                No	            Yes	        {}* or set()	    {5.7, 4, 'yes'}
Dictionary	        No	            No**	    { } or dict()	    {'Jun': 75, 'Jul': 89}
* You can use curly braces to define a set like this: {1, 2, 3}. However, if you leave the curly 
  braces empty like this: {} Python will instead create an empty dictionary. So to create an empty set, use set().
** A dictionary itself is mutable, but each of its individual keys must be immutable.
'''

'''
List         mutable        ordered      sortable      to add -- .append      []
Tupple       im-mutable     ordered      sortable      to add -- .append      ()
Set          mutable        unordered    un-sortable   to add -- .add         {}
Dictionary   mutable        unordered    un-sortable   to add -- .update      {}
'''
'''
Quiz: List Indexing
Use list indexing to determine how many days are in a particular month based 
on the integer variable month, and store that value in the integer variable num_days. 
For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.

Remember to account for zero-based indexing!
'''
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days=days_in_month[month-1]

print(num_days)


'''
#####Lists - mutable and ordered
'''
'''
Quiz: Slicing Lists
Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
'''
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


'''
What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)
'''
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

'''
Length of list
'''
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(arr[0])
print(arr[2:6])
print(arr[:3])
print(arr[4:])

'''
#####Tuples -  im-mutable and ordered
'''
tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])

'''
#####Sets - mutable and unordered
'''
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)


'''
#####Dictionary - Like sets with values
key:value
Key must be im-mutable
'''
'''
Quiz: Define a Dictionary
Define a dictionary named population that contains this data:

Keys	Values
Shanghai	17.8
Istanbul	13.3
Karachi	13.0
Mumbai	12.5
'''
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
population = {'Shanghai':17.8,
              'Istanbul':13.3,
              'Karachi':13.0,
              'Mumbai':12.5}
print(population['Mumbai'])


'''
Quiz: Adding Values to Nested Dictionaries
Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' 
to each dictionary in the elements dictionary. After inserting the new entries you should 
be able to perform these lookups:
'''
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print(elements)
# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
print(elements)


'''
Quiz: Count Unique Words
Your task for this quiz is to find the number of unique words in the text. 
In the code editor below, complete these three steps to get your answer.

Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
Convert the list into a data structure that would keep only the unique elements from the list.
Print the length of the container.
'''
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

'''
Quiz: Verse Dictionary
In the code editor below, you'll find a dictionary containing the unique words of verse stored as keys 
and the number of times they appear in verse stored as values. Use this dictionary to answer the following 
questions. Submit these answers in the quiz below the code editor.

Try to answer these using code, rather than inspecting the dictionary manually!

How many unique words are in verse_dict?
Is the key "breathe" in verse_dict?
What is the first element in the list created when verse_dict is sorted by keys?
Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. 
Use this list of keys to answer the next two questions as well.
Which key (word) has the highest value in verse_dict?
'''

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(set(verse_dict))
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = 'breathe' in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(max(sorted_keys)) 