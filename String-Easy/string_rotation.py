#Tricky question

class Solution():
    def stringRotation(self,s1,s2):
        if len(s1) != len(s2):
            return False
        s1 = s1 + s1
        if s2 in s1:
            return True
        return False

if __name__ == '__main__':
    user_input = input("Enter the strings by space separation : ")
    s1,s2 = user_input.split(" ")
    sol = Solution()
    print(sol.stringRotation(s1,s2))
