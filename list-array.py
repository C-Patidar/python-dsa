class Solution:
    def sollist(self,l):
        if len(l) <= 1:
            return 0
        result = []
        temp = 1
        for i in range(len(l)):
            for j in range(len(l)):
                if i == j:
                    continue
                temp = temp*l[j]
            result.append(temp)
            temp = 1

        return result

if __name__=='__main__':
    user_input = input("Enter the list interger by sapce separatioin :")
    l = list(map(int,user_input.split()))
    sol = Solution()
    print(sol.sollist(l))