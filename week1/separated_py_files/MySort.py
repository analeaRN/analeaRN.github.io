def my_sort(list_things):
    """
     Assignment 2.6, From memory, Don't look it up

     function that takes a list and returns a sorted version.  
     For instance, my_sort([3,1,2]) should return the list [1,2,3]. 

     @param list of things that can be ordered
    """

    # Hi Merge Sort
    def merge(left_list, right_list):
        result = []
        left_index = 0
        right_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                result.append(left_list[left_index])
                left_index += 1
            else:
                result.append(right_list[right_index])
                right_index += 1
        
        # check if left has leftovers
        if left_index < len(left_list):
            for index in range(left_index, len(left_list)):
                result.append(left_list[index])
        # check if right has leftovers
        if right_index < len(right_list):
            for index in range(right_index, len(right_list)):
                result.append(right_list[index])
        
        return result

    def mergesort(lst):
        if len(lst) <= 1: # Reach sorted list, go up and merge into order
            return lst
        
        mid = len(lst) // 2
        right_list = mergesort(lst[:mid])
        left_list = mergesort(lst[mid:len(lst)])
        return merge(right_list, left_list)

    return mergesort(list_things)

print("Let's sort the list [3, 2, 1]:", my_sort([3, 2, 1]))