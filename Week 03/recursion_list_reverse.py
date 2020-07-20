# file: recursion_list_reverse.py
#    A simple program that reverses the order of a list using recursion as its method.
# by: Charles Frelund

def my_list():
    myList = ["s", "t", "r", "a", "w"]
    return myList


def get_list_length():
    return len(my_list())

# recursive function which creates the new list.


def reverse_list(newList, x):
    if x < 0:  # because an index would end at zero, a less than 0 is used as the base case.
        return
    else:
        # calls the newList and appends (adds) the item based on the index argument provided.  Then recursively calls itself again.
        return newList.append((my_list()[x])), reverse_list(newList, x - 1)


def main():
    print(my_list())  # Original list.
    newList = []  # Instantiating the new reversed list.
    # The negative one offsets the get_list_length count to account for the index of the list.
    reverse_list(newList, get_list_length() - 1)
    print(newList)  # Prints the new list.


if __name__ == "__main__":
    main()
