#Sliding window problem

class Solution:
    def substring(self,s):
        max_len = 0
        left = 0
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left +=1
            char_set.add(s[right])
            max_len = max(max_len,right-left+1)
        return max_len

if __name__=='__main__':
    user_input = input("Enter the string : ")
    sol = Solution()
    print(sol.substring(user_input))