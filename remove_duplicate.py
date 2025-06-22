
class Solution:
    def remove_duplicate (self,arr):

        if len(arr) ==1:
            return 1

        freq = {}
        for i in arr :
            if i not in freq:
                freq[i] = 1
        return len(freq)



if __name__ == '__main__':
    user_input = input("Enter the elements : ")
    arr = list(map(int,user_input.split()))
    sol = Solution()
    print(sol.remove_duplicate(arr))

# if __name__ == '__main__':
#     user_input = input("enter the elements of the array : ")
#     arr = list(map(int,user_input.split()))
#     arr = set(arr)
#     print(len(arr))
