class Solution():
    def nonRepeat(self,s):
        if len(s) == 1:
            return s
        freq = {}
        for i in s :
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i,count in freq.items():
            if count == 1:
                return i
        return "No duplicate"

if __name__ == '__main__':
    user_input = input("Enter the string :")
    sol= Solution()
    print(sol.nonRepeat(user_input))