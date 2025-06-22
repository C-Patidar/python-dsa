
class Solution :
    def rotate(self,arr):
        last = len(arr)-1
        temp = arr[0]

        for i in range(0,len(arr)-1):
            arr[i] = arr[i+1]

        arr[last] = temp

        return arr


if __name__ == '__main__':
    user_input = input("Enter the elements of the array ")
    arr = list(map(int,user_input.split()))
    sol = Solution()
    print(sol.rotate(arr))