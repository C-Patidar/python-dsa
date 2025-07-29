class Solution():
    def removeDuplicate(self,s):
        if len(s) == 1:
            return s
        freq={}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        s1 = " "
        for i in freq.keys():
            s1 = s1 + i
        return s1



if __name__ == '__main__':
    user_input = input("Enter the string :")
    sol = Solution()
    print(sol.removeDuplicate(user_input))