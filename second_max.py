# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")


class Solution:
    def largestElement(self, arr):
        largest = arr[0]
        sec_largest = None

        for i in arr:
            if(i>largest):
                largest = i

        for i in arr :
            if i != largest:
                if sec_largest is None or i>sec_largest:
                    sec_largest = i

        return f"{largest} {sec_largest}"



if __name__ == '__main__':
    user_input = input("Enter the input :- ")
    arr = list(map(int, user_input.split()))
    sol = Solution()
    print(sol.largestElement(arr))