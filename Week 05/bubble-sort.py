# bubble-sort.py
#     A simple program which demonstrates a bubble-sort using a list.
# by: Charles Frelund

def bubbleSort(list):
    # Traverse through all elements in the list.
    for passnum in range(len(list)-1, 0, -1):
        for listItem in range(passnum):
            if list[listItem] > list[listItem + 1]:
                listItemTempStore = list[listItem]
                list[listItem] = list[listItem + 1]
                list[listItem + 1] = listItemTempStore

                #Prints out the list though each step to help demonstrate how the numbers are selected and repositioned.
                print(list)
            print(list, "1111")
        print(list, "2222")
    print(list, "3333")

myList = [10, 2, 7, 6, 9, 8, 1, 3, 4, 5]
bubbleSort(myList)
print(myList)
