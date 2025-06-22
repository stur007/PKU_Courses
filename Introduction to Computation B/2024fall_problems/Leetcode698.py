from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        per_tot = tot // k
        if per_tot * k != tot:
            return False
        nums.sort(reverse=True)
        if nums[0] > per_tot:
            return False
        test = [0] * k

        def f(idx):
            if idx == len(nums):
                return sum(test) == tot
            for j in range(len(test)):
                if j >0 and test[j] == test[j-1]:
                    continue
                if test[j] + nums[idx] <= per_tot:
                    test[j] += nums[idx]
                    if f(idx + 1):
                        return True
                    test[j] -= nums[idx]
            return False
        return f(0)

# 感觉优化的还可以！