class solution:


    def maxArea(self, height: list[int]):

        l = 0
        r = len(height) - 1
        result = 0

        while l<len(height) and l<r:

            area = (r-l) * min(height[l], height[r])
            result = max(result, area)

            if height[l] < height[r]:
                l += 1

            else:
                r -= 1


        return result


check = solution()
height = [1,8,6,2,5,4,8,3,7]
print(check.maxArea(height))