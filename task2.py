def subtask1() -> None:
    # subtask 1
    integer = int(input("Input an integer: "))
    floater = float(input("Input a float: "))
    stringer = input("Input a string: ")
    booleaner = input("Input a boolean (True/False): ").lower() == "true"

    print("The integer is: " + str(integer))
    print("The float is: " + str(floater))
    print("The string is: " + stringer)
    print("The boolean is: " + str(booleaner))


def subtask2() -> None:
    # subtask 2
    zahl = 10
    kommazahl = 10.5
    text = "Hello, World!"
    wahrheitswert = True
    print("The type of zahl is: " + str(type(zahl)))
    print("The type of kommazahl is: " + str(type(kommazahl)))
    print("The type of text is: " + str(type(text)))
    print("The type of wahrheitswert is: " + str(type(wahrheitswert)))


if __name__ == "__main__":
    # subtask1()
    subtask2()
