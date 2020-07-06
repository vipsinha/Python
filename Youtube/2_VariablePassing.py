# Print variable messages
my_message  = 'Hello World'
my_message_doublequote  = "Vipul's World -- Double quote"
my_message_singlequote  = 'Vipul\'s World -- Single quote'

greeting = 'Hello'
name = 'Vipul'

print (my_message)
print (my_message_doublequote)
print (my_message_singlequote)
print (len(my_message))
print (my_message[0])
print (my_message[10])

# gives error 
# print (my_message[11])

# 0 start, 5 length
print (my_message[0:5])

#slicing
print (my_message[:5])

#slicing
print (my_message[6:])

# message to lower case
print(my_message.lower())

# message to uper case
print(my_message.upper())

# count the number of lestters in the message
print(my_message.count('l'))

# count the number of word in the message
print(my_message.count('World'))

#replace will NOT change the same string 
new_message = my_message.replace('World', 'Universe')
print (new_message)
print (my_message)

#replace will change the same string 
my_message = my_message.replace('World', 'Universe')
print (my_message)

my_greeting = greeting + ', ' + name
my_greeting_improved = f'{greeting}, {name}. Improved'

print(my_greeting)
print(my_greeting_improved)

# to see the attributes can be used
# print(dir(name))

# to get the help
# print(help(str))
print(help(str.lower))