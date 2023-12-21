class solution:


    def lenghtOfLastWord(self, s:str):

        i = len(s)-1
        lenght= 0

        while i>=0 and s[i] == " ":
            i -= 1

        while i>=0 and s[i] != " ":
            lenght += 1
            i-=1

        return lenght


check_code = solution()
word = "hello world   "
print(check_code.lenghtOfLastWord(word))
