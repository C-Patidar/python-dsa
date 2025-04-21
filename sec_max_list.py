def max_in_arr(list1):

    if len(list1)< 2:
        return None

    max1 = None
    max2 = None

    for num  in list1:
        if num == max1 or num == max2:
            continue

        if max1 is None or num > max1:
            max2 = max1
            max1 = num
        elif max2 is None or num > max2:
            max2 = num

    return max2


if __name__ == '__main__':
    user_input = input("enter the number separeted by space: ")
    list1 = list(map(int, user_input.split()))
    print(list1)
    result = max_in_arr(list1)

    if result is None:
        print("No 2nd largest element is found")
    else:
        print(max_in_arr(list1))
