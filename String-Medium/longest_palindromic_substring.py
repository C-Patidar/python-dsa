class Solution:

    def expandaround(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -=1
            right +=1
        return s[left+1:right]
    def substring(self,s):

        if len(s) <= 1:
            return s
        longest = ''
        for i in range(len(s)):
            old_pal = self.expandaround(s,i,i)

            even_pal = self.expandaround(s,i,i+1)

            if len(old_pal) > len(longest):
                longest = old_pal
            if len(even_pal)> len(longest):
                longest = even_pal
        return longest

if __name__ == '__main__':
    user_input = input("Enter the string : ")
    sol = Solution()
    print(sol.substring(user_input))