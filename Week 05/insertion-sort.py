# selection-sort.py
#     A simple program which demonstrates a insertion sort using a list.
# by: Charles Frelund

def insertionSort(list):
    for index in range(1, len(list)):
        currentvalue = list[index]
        position = index

        while position > 0 and list[position - 1] > currentvalue:
            list[position] = list[position - 1]
            position = position - 1

            print(list, "FOR")
        
        #Prints out the list though each step to help demonstrate how the numbers are selected and repositioned.
        print(list, "WHILE")

        list[position] = currentvalue


myList = [10, 2, 7, 6, 9, 8, 1, 3, 4, 5]
insertionSort(myList)
print(myList)
