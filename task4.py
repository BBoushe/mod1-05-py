def fact(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == "__main__":
    user_input = int(input("Input an integer to calculate its factorial: "))
    print("Factorial of " + str(user_input) + " is: " + str(fact(user_input)))
