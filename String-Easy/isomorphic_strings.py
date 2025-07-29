class Solution():
    def isIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False

        map1 = {}
        map2 = {}

        for c1, c2 in zip(s1, s2):
            # Check mapping from s1 → s2
            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                map1[c1] = c2

            # Check mapping from s2 → s1
            if c2 in map2:
                if map2[c2] != c1:
                    return False
            else:
                map2[c2] = c1

        return True


if __name__ == '__main__':
    user_input = input("Enter two strings separated by space: ")
    s1, s2 = user_input.split(" ")
    sol = Solution()
    print("Isomorphic:", sol.isIsomorphic(s1, s2))
