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