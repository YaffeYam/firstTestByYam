# Printing a header indicating both "myZip True and False"
print("myZip True and False:")

# Function to demonstrate myZip when it works as expected
def myZip_true(it1, it2):
    print("myZip True:")
    
    # Example where myZip works as expected
    result = list(zip(it1, it2))
    print(result)
    print()

# Function to demonstrate myZip when it may not work as expected
def myZip_false(it1, it2):
    print("myZip False (please note that no error is provided in VSCode):")
    
    try:
        # Using myZip to combine elements from it1 and it2
        result = list(zip(it1, it2))
        print(result)  # This won't be executed if an exception is raised
    except ValueError as e:
        print(e)
        raise  # Re-raise the ValueError to stop program execution
    print()

# Running the examples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
myZip_true(list1, list2)

list3 = [1, 2, 3]
list4 = ['a', 'b']
myZip_false(list3, list4)