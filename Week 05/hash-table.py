# hash-table.py

# Creates an empty hash table to insert items into.
def create_empty_hash_table(size):
    myList = []
    for i in range(size):
        myList.append(None)
    return myList

# Allows the user to input the quantity of items to insert into the table.
def item_qty():
    itemQty = int(input("How many items would you like to insert? "))
    return itemQty


def insert_item_using_hash_method():
    myItem = int(input("Item to insert? "))
    return myItem


def main():
    desiredTableSize = int(
        input("What is the size of the desired hash table? "))
    myHashTable = create_empty_hash_table(desiredTableSize)
    print(myHashTable)

    qtyOfItemsToInsert = item_qty()
    for i in range(qtyOfItemsToInsert):
        myItem = insert_item_using_hash_method()
        hashLocation = myItem % desiredTableSize
        myHashTable[hashLocation] = myItem
        print(myHashTable)

    print(myHashTable)


if __name__ == "__main__":
    main()
