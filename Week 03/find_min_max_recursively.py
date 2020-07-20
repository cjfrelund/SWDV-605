# find_min_max_recursively.py
#     A simple program that finds the min and max values of a list recursively.
# by: Charles Frelund

# Demo list to traverse and find min and max values for.
def my_list():
    myList = [4, 8, 22, 3, 96, 5, 2]  # Random ordered list.
    return myList


# recursive function to find the min value of my_list().
def find_min_value(list, n):
    if (n == 1):
        return list[0]
    # Itterates through each number in the list using recursion.
    return min(my_list()[n-1], find_min_value(my_list(), n - 1))


# recursive function to find the max value of my_list().
def find_max_value(list, n):
    if (n == 1):
        return list[0]
    # Itterates through each number in the list using recursion.
    return max(my_list()[n-1], find_max_value(my_list(), n - 1))


def main():
    try:
        # finds the length of the list to find the max and min values from.
        n = len(my_list())
        print("The min value in the list is...", find_min_value(my_list(), n))
        print("The max value in the list is...", find_max_value(my_list(), n))
    except:
        print("Not a valid list. List must contain at least one item.")


if __name__ == "__main__":
    main()
