class solution:

    def mojorityElement(self, nums:list[int]):

        n = len(nums)
        element_count = dict(int)

        for number in nums:

            element_count[number] +=1


        n = n//2
        for key, value in element_count:
            if value > n:
                return key

        return 0