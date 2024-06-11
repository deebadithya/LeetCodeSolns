

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        splitting the result into two seperate list first one will storing the elements in arr1 and also arr2 including its n times of count with these same order in arr2

        and second list stores the remaining element of arr1 which is not in arr2 in sorted order.

        and finally we joining these two as final result.

        runtime: 37 ms
        memory: 16.61 mb
        """


        first_ls = []
        second_ls = []
        for j in arr2:
            first_ls.extend([j] * arr1.count(j))
        for i in arr1:
            if i not in arr2:
                second_ls.append(i)
        second_ls = sorted(second_ls)
        return first_ls + second_ls

        
