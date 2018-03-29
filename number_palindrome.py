def number_palindrome():
    try:
        num1 = input("Write your number here: ")
        num1 = str(int(num1))
        if num1 == num1[::-1]:
            print(True)
        else:
            print(False)
    except Exception:
        print("That's not a number!!!")
        number_palindrome()


number_palindrome()