class solution:

    def strStr(self, haystack: str, needle:str):

        if needle == "":
            return 0

        for i in range(len(haystack)+1 - len(needle)):
            for j in range(len(needle)):

                if haystack[i+j] != needle[j]:
                    break

                if j == len(needle) -1:
                    return i

        return -1


First_occurance = solution()
haystack = "hello"
needle = "ll"

print(First_occurance.strStr(haystack,needle))