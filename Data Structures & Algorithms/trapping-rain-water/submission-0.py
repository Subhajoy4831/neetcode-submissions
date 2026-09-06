class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        res = 0
        for i in range(len(height)):
            if i == 0:
                left[i] = height[i]
            else:
                if height[i]>left[i-1]:
                    left[i] = height[i]
                else:
                    left[i] = left[i-1]
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                right[i] = height[i]
            else:
                if height[i]>right[i+1]:
                    right[i]=height[i]
                else:
                    right[i]=right[i+1]
        for i in range(len(height)):
            res += min(left[i],right[i]) - height[i]
        return res