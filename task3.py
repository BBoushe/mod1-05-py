if __name__ == "__main__":
    integer = 10
    f_integer = float(integer)
    print("The converted integer is: " + str(integer))

    floater = 10.4932
    i_floater = int(floater)
    print("The converted float is: " + str(i_floater))

    integer = 5
    stringer = str(integer)
    print("The converted integer is: " + stringer)

    s_w_integer = "string with integer 10"
    s_int = int(s_w_integer.split()[-1])

    inti = 123.1  # as long as it's not 0 it's going to be true
    bolli = bool(inti)
    print("The converted integer is: " + str(bolli))
