class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []        # To store the final result
        count = 0          # Balance counter
        start = 0          # Start index of a primitive

        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:  # s[i] == ')'
                count -= 1

            # If count becomes zero, it means we have found a full primitive
            if count == 0:
                # Exclude the outermost parentheses: s[start+1 to i-1]
                result.append(s[start + 1:i])
                start = i + 1  # Start of the next primitive

        return ''.join(result)

# --------------------------
if __name__ == '__main__':
    s = input("Enter the parentheses string: ")
    sol = Solution()
    print("After removing outermost parentheses:", sol.removeOuterParentheses(s))