# Remove Duplicates from List: Create a function remove_duplicates that takes a list and returns a new list with duplicate elements removed.

def test01(arr):
    empty = []
    arr.sort()

    for i in arr:
        if i not in empty:
            empty.append(i)
        else: 
            print("NOT NICE")
    print(empty)
    
test01([1,2,3,3,3,4,2,1])

