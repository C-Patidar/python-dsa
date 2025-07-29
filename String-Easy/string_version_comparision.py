class Solution:
    def stringVersionComparision(self, s1, s2):
        v1 = list(map(int, s1.split('.')))
        v2 = list(map(int, s2.split('.')))

        # Pad the shorter list with zeros
        max_len = max(len(v1), len(v2))
        v1 += [0] * (max_len - len(v1))
        v2 += [0] * (max_len - len(v2))

        for i in range(max_len):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0


if __name__ == '__main__':
    s1, s2 = input("Enter the versions (space separated): ").split()
    sol = Solution()
    print(sol.stringVersionComparision(s1, s2))
