# Python 3 code to rotate an array
# and answer the index query
 
# Function to compute the element 
# at given index
def findElement(arr, ranges, rotations, index) :
     
    for i in range(rotations - 1, -1, -1 ) :
     
        # Range[left...right]
        left = ranges[i][0]
        right = ranges[i][1]
        print(left, right)
 
        # Rotation will not have 
        # any effect
        if (left <= index and right >= index) :
            print(index, arr[index])
            if (index == left) :
                index = right
            else :
                index = index - 1
         
    # Returning new element
    return arr[index]

if __name__ == '__main__':
# Driver Code
    arr = [ 1, 2, 3, 4, 5 ]
 
# No. of rotations
    rotations = 2
 
# Ranges according to 
# 0-based indexing
    ranges = [ [ 0, 4 ], [ 0, 6 ] ]
 
    index = 1
 
    print(findElement(arr, ranges, rotations, index))