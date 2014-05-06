#Sorting

##Pseudocode for a swap

'''python
BEGIN
INPUT list, index of item to swap
SET a to index'th item in list
SET b to (index+1)th item in list
SET (index)th item in list to b
SET (index +1 )th item in list to a
OUTPUT list
END
'''

##Pseudocode for bubble sort

'''python
BEGIN
INPUT alist
SET swaps to True
WHILE swaps is True:
    SET Swaps to False
    FOR item in alist:
        IF item > next item:
            Swap item and next item
            Set Swaps to True
OUTPUT alist
END
'''
