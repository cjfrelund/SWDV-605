# selection-sort.py
#     A simple program which demonstrates a selection sort using a list.
# by: Charles Frelund


def selectionSort(list):
    # Traverse through all elements in the list.
    for fillslot in range(len(list) -1, 0, -1):
        maxpos = 0
        for location in range(1, fillslot + 1):
            if list[location] > list[maxpos]:
                maxpos = location

        #Prints out the list though each step to help demonstrate how the numbers are selected and repositioned.
        print(list)

        temp = list[fillslot]
        list[fillslot] = list[maxpos]
        list[maxpos] = temp

    print(list, "0000")


myList = [10, 2, 7, 6, 9, 8, 1, 3, 4, 5]
selectionSort(myList)
print(myList)
