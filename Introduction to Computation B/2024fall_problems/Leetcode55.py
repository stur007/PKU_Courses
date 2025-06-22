from collections import deque
from heapq import heappush
from typing import List
import heapq

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums)-1
        if final == 0:
            return True
        q = deque([0])
        visited = []
        heappush(visited, 0)
        while q:
            x = q.popleft()
            step = nums[x]
            for dx in range(visited[-1]+1-x, min(step, final - x) + 1):
                nx = x + dx
                if nx == final:
                    return True
                else:
                    if nx not in visited:
                        heapq.heappush(visited, nx)
                        q.append(nx)
        return False
sol= Solution()
print(sol.canJump([1,1,1,0]))