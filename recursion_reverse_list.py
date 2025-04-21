def reverse_list(list1):
    if len(list1)<=1:
       return list1
    return reverse_list(list1[1:])+[list1[0]]

if __name__ == '__main__':
    user_input = input("enter the number separeted by space: ")
    list1 = list(map(int, user_input.split()))
    print(list1)
    reverse_list(list1)
    print("reverse list using the recursion is : ", reverse_list(list1))