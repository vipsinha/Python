'''
Error Handling
'''

try:
    # some code
    print("In try block\n")
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))


try:
    # some code
    print("In Try Block\n")
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
finally:
    print("Always this line will execute")