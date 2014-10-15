def quicksort (input_list):
    
    if(len(input_list) <= 1):
        return input_list
    
    beforePivot = []
    # make a third equal to pivot list to make sure lists that have many elements equal to pivot
    # do not descend into worst case
    equalToPivot = []
    afterPivot = [] 
    
    #choose median of three to optimize pivot choice
    if(input_list[0] < input_list[len(input_list) - 1] and input_list[0] > input_list[len(input_list)/2]):
        pivot = input_list[0]
    elif(input_list[len(input_list) - 1] < input_list[0] and input_list[len(input_list) - 1] > input_list[len(input_list)/2]):
        pivot = input_list[len(input_list) - 1]
    else:
        pivot = input_list[len(input_list)/2]
    
    #sort list into three sublists by pivot
    for element in input_list:
        if(element > pivot):
            afterPivot.append(element)
        elif(element < pivot):
            beforePivot.append(element)
        else:
            equalToPivot.append(element)
            
    #recursive step   
    head = quicksort(beforePivot)
    tail = quicksort(afterPivot)
    
    return head + equalToPivot + tail
    
    
empty_list = []
print quicksort(empty_list)

inorderList = [1,2,3,4]
print quicksort(inorderList)

outoforderList = [4, 9, 3 ,7, 2, 1, 0, 5, 9, 11, 11, 8]
print quicksort(outoforderList)

negativesList = [ 4, 3, 1, -2, -6, -7, -3, -2]
print quicksort(negativesList)

wordsList = ["heybuddy", "pytest", "help", "coffee", "jpeg", "raisinbran"]
print quicksort(wordsList)


