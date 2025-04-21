#Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

#The Greatest Common Divisor of any two integers is the largest number that divides both integers.

class Solution():
    def gcd(self,a,b):
        gcd = 1
        for i in range(1, min(a,b)+1):
            if a % i ==0 and b % i ==0:
                gcd = i
        return gcd

if __name__ == '__main__':
    user_input = input("Enter the two number separated by space :- ")
    n,m = map(int, user_input.split())
    sol = Solution()
    print("GCD :- ", sol.gcd(n,m))


    '''
    class Solution:
    def findGCD(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    '''
