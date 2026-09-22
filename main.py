from math import pi

if __name__ == "__main__":
    radius = float(input("Input the radius of the circle: "))
    print(
        "The area of the circle with radius "
        + str(radius)
        + " is: "
        + str(round(pi * radius**2, 2))
    )
