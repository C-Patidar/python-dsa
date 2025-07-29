if __name__ == '__main__':
    s = input("Enter the string :")
    def checkBinary(s):
        if s.isdecimal():
            for i in s :
                if i != '0' and i != '1':
                    return False
            return True
        return False
    print(checkBinary(s))