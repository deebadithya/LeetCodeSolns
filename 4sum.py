"""
4sum.py
"""
# def fourSum(nums, target):
#     nums.sort()
    
#     def sum4(nums, target, count=0):
#         if count == 4 and target == 0:
#             return [[]]
#         if count == 4:
#             return None
#         result = []
#         for i in range(len(nums)):
#             count_result = sum4(nums[i+1:], target - nums[i], count+1)
#             if count_result:
#                 for ind in range(len(count_result)):
#                     count_result[ind] = [nums[i]] + count_result[ind]
#                 for res in count_result:
#                     if res not in result:
#                         result.extend([res])
#         return result
#     return sum4(nums, target)
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            # skip duplicate starting values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums) - 2):
                # skip duplicate starting values
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
                

# result = fourSum([1,0,-1,0,-2,2], 0)
# result = fourSum([2,2,2,2,2], 8)
result = fourSum([-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481], -5617)
print(result)