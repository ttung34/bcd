import functools

class Solution:

    def rob(self, nums:list[int])-> int:
        def dfs(i):
            if i<0: 
                return 0
            