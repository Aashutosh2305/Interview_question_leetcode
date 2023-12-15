class solution:


    def removeElement(self, nums:list[int], val:int):

        # k as pointer

        k = 0
        for i in range(len(nums)):

            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


instance_solution = solution()

nums = [3,2,2,3]
val = 2
instance_solution.removeElement(nums,val)

