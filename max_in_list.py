
def find_max(list1):

    if not list1:
        return None

    max = list1[0]
    for i in range(len(list1)):
        if(list1[i]>max):
            max = list1[i]
    return max

if __name__ == '__main__':
    user_input = input("Enter the numbers separated by a space: ")
    list1 = list(map(int, user_input.split()))
    print(list1)
    print("Max no. in the list is: ",find_max(list1))

