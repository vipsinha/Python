
print('#####my module#####')

test = 'Test String'

def find_index (list, item):
    for num, value in enumerate (list):
        if (value == item):
            return num
    return -1
