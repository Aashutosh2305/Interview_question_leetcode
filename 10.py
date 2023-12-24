class solution:


    def twoSum(self, numbers: list[int], target: int):


        left = 0
        right = len(numbers) -1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1

            else:
                left += 1


        return [left+1, right+1]



check = solution()
numbers = [2,7,11,15]
target = 9
print(check.twoSum(numbers, target))