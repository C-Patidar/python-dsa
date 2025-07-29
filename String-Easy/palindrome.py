import cgi


class Solution:
    def isPalindrome(self,s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        right = len(s)-1
        left = 0

        while left<right :
            if s[left]!=s[right]:
                return False
            left = left+1
            right = right-1
        return True


if __name__ == '__main__':
    s = input("Enter the string: ")
    sol = Solution()
    print("isPalindrome :  ",sol.isPalindrome(s))
