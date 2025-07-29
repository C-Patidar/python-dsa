
class Solution:
    def reverseString(self,s):
        l = list(s)
        left = 0
        temp = 0
        right = len(s)-1
        while left<right:
            temp = l[left]
            l[left] = l[right]
            l[right] = temp
            left = left +1
            right = right -1

        return ''.join(l)
        #return s[::-1]

if __name__ == '__main__':
    s = input("Enter the string : ")
    sol = Solution()
    print("Reverse string is : ", sol.reverseString(s))