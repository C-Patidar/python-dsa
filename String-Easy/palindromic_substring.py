class Solution():
    def palindromicSubstring(self,s):

        count = 0
        n = len(s)

        # Generate all substrings using two nested loops
        for i in range(n):  # Start index
            for j in range(i, n):  # End index
                sub = s[i:j + 1]  # Substring from i to j
                if sub == sub[::-1]:
                    #print(sub)# Check if palindrome
                    count += 1

        return count

if __name__ == '__main__':
    s = input("Enter the string :")
    sol = Solution()
    print(sol.palindromicSubstring(s))