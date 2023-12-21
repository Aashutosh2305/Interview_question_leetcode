class solution():

    def validPolindrom(self, s:str):

        # Method-1

        # NewStrs = ''
        #
        # for c in s:
        #
        #     if c.isalnum():
        #         NewStrs = c.lower()
        #
        # return NewStrs == NewStrs[::-1]

        #Method - 2

        l , r = 0, len(s) -1
        while l<r:

            while l<r and not self.alphanum(s[l]):
                l += 1

            while r>l and not self.alphanum(s[r]):
                r-=1

            l, r =  l+ 1 , r-1


            if s[l] != s[r]:
                return False

        return True






        # Making fuction for Alphanumeric condtiond

    def alphanum(self, c):

        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord('z') or
            ord("0") <= ord(c) <= ord('9')
        )


questions = solution()
s = "A Man, a plan, a canal, : panama"
print(questions.validPolindrom(s))