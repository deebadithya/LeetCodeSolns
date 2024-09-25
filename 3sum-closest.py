from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lf, rt = i+1, len(nums) - 1
            while rt > lf:
                current_sum = nums[i] + nums[lf] + nums[rt]
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum < target:
                    lf += 1
                elif current_sum > target:
                    rt -= 1
                else:
                    return current_sum

        return closest_sum



soln = Solution()
result = soln.threeSumClosest([-1,2,1,-4], 1)
print(result)
