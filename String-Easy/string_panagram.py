class Solution():
    def stringPanaram(self,s):
        s = s.lower()
        s = ''.join([char for char in s if char.isalpha()])
        if len(s) < 26:
            return False
        final = set(s)
        if len(final)<26:
            return False
        return True

if __name__ == '__main__':
    user_input = input("Enter the string via space separator :")
    sol = Solution()
    print(sol.stringPanaram(user_input))