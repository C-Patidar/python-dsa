class Solution():
    def countOccurence(self,s):
        freq = {}
        for i in s :
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return freq.items()


if __name__ == '__main__':
    user_input = input("Enter the string :")
    sol = Solution()
    for item, count in sol.countOccurence(user_input):
        print(f'{item}:{count}')
