#Sorting

This ia a model set of answers for the sorting unit.  refer to http://ams-ict.github.io/GCSEcomputing/u2.html

## Introduction
Sorting is a common activity.  We often need to sort things in an order to make the output better for humans to read, or to process things in a given order.

##Algorithms used in this project
###Pseudocode for a swap


```
BEGIN
INPUT list, index of item to swap
SET a to index'th item in list
SET b to (index+1)th item in list
SET (index)th item in list to b
SET (index +1 )th item in list to a
OUTPUT list
END
```

###Pseudocode for bubble sort


```
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
```
### pseudocode for  finding the minimum (mini())
```
BEGIN
INPUT alist
SET answer to first item of list
FOR EACH number in alist:
    IF number < answer:
        set answer to number
OUTPUT answer
END
```
### pseudocode for Selection sort 
```
BEGIN
INPUT alist
set answer to [] (an empty list)
WHILE length of alist > 0:
    set N to minimum of alist (see previous code)
    remove N from alist
    append N to answer
OUTPUT answer
END
```
## Testing
###Swap Criteria
The swap function will be successful if
it accepts a list and an index as input
it returns the list with the indexed item swapped with its next item.

----
example input|Expected output
----
[4,3,2,1], 1|[4,2,3,1]
----
[4,3,2,1], 0|[3,4,2,1]
----
[1,2], 0|[2,1]
---