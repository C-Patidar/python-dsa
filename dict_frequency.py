from selenium.webdriver.common.devtools.v118.page import print_to_pdf


def count_frequency(list1):
    frq_dict = {}

    for i in list1:
        if i in frq_dict:
            frq_dict[i] = frq_dict[i]+1
        else:
            frq_dict[i] = 1

    return frq_dict

if __name__ == '__main__':
    user_input = input("Enter the no. having space between them :")
    list1 = list(map(int, user_input.split()))
    print(count_frequency(list1))