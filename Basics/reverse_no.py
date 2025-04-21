class Solution:
    def reverse(self,n):
        rev = 0
        n = abs(n)

        while n>0:
            digit = n % 10
            rev = rev * 10 + digit
            n = n//10

        return rev

if __name__ == '__main__':
    user_input = int(input("Enter the no. "))
    sol = Solution()
    print(sol.reverse(user_input))