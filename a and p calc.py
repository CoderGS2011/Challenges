print("Kindly, write the answers in small letters.")
operation = input(
    "Write the operation which you want to run. Area or perimeter.")
shape = input("Which shape's " + operation +
              " do you want to know?Square or rectangle. \n")
if shape == "square" and operation == "perimeter":
    side = int(input("Write the length of the square."))
    print("The answer is", side * 4)

if shape == "square" and operation == "area":
    side = int(input("Write the length of the square."))
    print("The answer is", side * side)

if shape == "rectangle" and operation == "perimeter":
    l = int(input("Write the length of the rectangle."))
    w = int(input("Write the width of the rectangle."))
    print("The answer is", 2 * l + w)

if shape == "rectangle" and operation == "area":
    l = int(input("Write the length of the rectangle."))
    w = int(input("Write the width of the rectangle."))
    print("The answer is", l * w)

print("Thanks for using our calculator!")
