# Problem Statement: Given an integer N, return true if it is a palindrome else return false.
#
# A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

class Solution:
    def palindrom(self, n ):
        rev = 0
        n = abs(n)
        dup = n

        while n > 0:
            digit  = n % 10
            rev = rev *10 +digit
            n = n//10

        if rev == dup:
            return True
        else:
            return False


if __name__ == '__main__':
    user_input = int(input("Enter the no. : "))
    sol = Solution()
    print(sol.palindrom(user_input))