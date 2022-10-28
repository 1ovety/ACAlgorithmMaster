# Question 35. Search Insert Position

# binary search :
# Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. 
# The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).
# 
# reference from https://www.geeksforgeeks.org/binary-search/


class Solution:
    def searchInsert (v, To_Find):
        lowNum = 0
        highNum = len(v) - 1

        # All cases check
        # for mid = lo-(hi-lo)/2
       

        while highNum - lowNum > 1:

            mid = (highNum + lowNum) // 2

            if v[mid] < To_Find:
                lowNum = mid + 1

            else:
                highNum = mid
                
        if v[lowNum] == To_Find:
            
            return lowNum
            
        elif v[highNum] == To_Find:
          
            return highNum
        
        else:
            
            print("There is no position")