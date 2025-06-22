

class Solution :
    def is_arr_sort(self,arr):
        if len(arr) == (0 or 1):
            return True

        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                continue
            else:
                return False
        return True




if __name__ == '__main__':
    user_input  = input("Enter the elements of the array :")
    arr = list(map(int, user_input.split()))
    is_sort = Solution()
    print(is_sort.is_arr_sort(arr))