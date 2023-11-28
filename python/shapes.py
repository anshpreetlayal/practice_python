#calculating area of rectangle
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Taking user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))


#  area of the rectangle
area_of_rectangle = calculate_rectangle_area(length, width)
print(f"The area of the rectangle with length {length} and width {width} is: {area_of_rectangle}")

#Area of cirlce

#Area of triangle

# Area of square
def calculate_square_area(side):
    area = side**2
    return area


# Taking user input for the side of the square
side = float(input("Enter the side length of the square: "))
