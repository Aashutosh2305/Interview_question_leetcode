class solution:

    def merge(self, num1: list[int], m: int, num2:list[int], n:int):

        # last index of num1 array
        last = m+n-1

        while m>0 and n>0:
            if num1[m-1] > num2[n-1]:
                num1[last] = num1[m-1]
                m -=1

            else:
                num1[last] = num2[n-1]
                n -=1

            last -=1

        # edge case (fill num1 leftover num2 element)

        while n>0:
            num1[last] = num2[n-1]
            n, last = n-1, last-1



solution_instance = solution()

num1 = [1,2,3,0,0,0]
num2 = [2,5,6]
m = 3
n = 3
solution_instance.merge(num1,m,num2,n)

print(num1)