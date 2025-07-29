from xml.sax.handler import feature_string_interning


class Solution :
    def anagramStrings(self,s1,s2):
        if len(s1) != len(s2):
            return False
        freq={}
        for i in s1:
            if i in freq:
                freq[i] += 1
            else :
                freq[i] = 1
        for i in s2:
            if i in freq:
                freq[i] -= 1
            else :
                freq[i] = 1
        if all(value ==0 for value in freq.values()):
            return True
        return False


if __name__ == '__main__':
    user_input = input("Enter the string with separatingg by space : ")
    s1 , s2 = user_input.split(' ')
    sol = Solution()
    print(sol.anagramStrings(s1,s2))

