
def mergesort(input_list):
    
    if(len(input_list) <= 1):
        return input_list
    
    left_half = []
    right_half = []
    
    #split list in half
    for i in range(0,len(input_list)):
        if(i <= len(input_list)/2 - 1):
            left_half.append(input_list[i])
        else:
            right_half.append(input_list[i])
    
    #recursive steps
    left_half = mergesort(left_half)
    right_half = mergesort(right_half)

    leftIndex = 0
    rightIndex = 0 
    realListIndex = 0
    
    while (leftIndex < len(left_half) and rightIndex < len(right_half)):
        
        if(left_half[leftIndex] < right_half[rightIndex]):
            input_list[realListIndex] = left_half[leftIndex]
            realListIndex += 1
            leftIndex += 1
            
        else:
            input_list[realListIndex] = right_half[rightIndex]
            realListIndex += 1
            rightIndex += 1
    
    while(leftIndex < len(left_half)): #if the right_half has already been completely iterated through and left has not
        input_list[realListIndex] = left_half[leftIndex]
        realListIndex += 1
        leftIndex += 1
     
    while(rightIndex < len(right_half)):#if the left_half has already been completely iterated through and right has not
        input_list[realListIndex] = right_half[rightIndex]
        realListIndex += 1
        rightIndex += 1
    
    return input_list


empty_list = []
print mergesort(empty_list)

inorderList = [1,2,3,4]
print mergesort(inorderList)

outoforderList = [4, 9, 3 ,7, 2, 1, 0, 5, 9, 11, 11, 8]
print mergesort(outoforderList)

negativesList = [ 4, 3, 1, -2, -6, -7, -3, -2]
print mergesort(negativesList)

wordsList = ["heybuddy", "pytest", "help", "coffee", "jpeg", "raisinbran"]
print mergesort(wordsList)



    
    
    

