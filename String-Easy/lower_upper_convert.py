class Solution():
    def swapString(self,s):
        result = ''
        for i in s :
            ascii_value = ord(i)
            if 'a' <= i <= 'z':
                char = chr(ascii_value-32)
                result = result+char
            elif 'A' <= i <= 'Z':
                char = chr(ascii_value + 32)
                result = result + char
            else:
                result = result+i
        return result

if __name__ == '__main__':
    user_input = input("Enter the string : ")
    sol = Solution()
    print(sol.swapString(user_input))
