class Solution:
    def trap(self, height: list[int]) -> int:
        suffix_max_list = [len(height)] * len(height)
        prefix_max_list = [-1] * len(height)

        s_max = len(height)-1
        for i in range(len(height)-2, -1, -1):
            if height[s_max] <= height[i]:
                s_max = i
            else:
                suffix_max_list[i] = s_max

        p_max = 0
        for i in range(1, len(height)):
            if height[p_max] <= height[i]:
                p_max = i
            else:
                prefix_max_list[i] = p_max

        water = 0
        for i in range(len(height)) :
            if suffix_max_list[i] - prefix_max_list[i] > 1 and suffix_max_list[i] < len(height) and prefix_max_list[i] != -1:
                water += min(height[suffix_max_list[i]], height[prefix_max_list[i]]) - height[i]

        return water

