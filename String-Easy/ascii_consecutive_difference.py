class Solution:
    def asciiConsecutiveDifference(self,s):
        result = []
        for i in range(1,len(s)):
            result.append(abs(ord(s[i])-ord(s[i-1])))
        return ' '.join(str(x) for x in result)

if __name__=='__main__':
    user_input = input("Enter the string : ")
    sol = Solution()
    print(sol.asciiConsecutiveDifference(user_input))