'''
Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
'''
from selenium.webdriver.support.expected_conditions import none_of


class Solution:
    def armstrong(self, n):
        if n == 0:
            return True
        n = abs(n)
        m = n
        pow = len(str(n))
        sum = 0

        while n > 0:
            digit = n % 10
            sum = sum + digit ** pow
            n = n // 10
        if sum == m :
            return True
        else:
            return False


if __name__ == '__main__':
    user_input = int(input("Enter the no. :- "))
    sol = Solution()
    print(sol.armstrong(user_input))