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
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Taking user input for the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculating the area of the triangle
area_of_triangle = calculate_triangle_area(base, height)
print(f"The area of the triangle with base {base} and height {height} is: {area_of_triangle}")

# Area of square
def calculate_square_area(side):
    area = side**2
    return area
# Taking user input for the side of the square
side = float(input("Enter the side length of the square: "))
#area of square
area_of_square = calculate_square_area(side)
print(f"The area of the square with side length {side} is: {area_of_square}")
