#First class are functions that you can pass to another function as parameter and still you can use them as function.
#They can also be stored in variables and returned as a value.
def square(number):

	return number * number


def calculate_area_of_circle(func,radius, pi):

	return (func(radius) * pi)


result = calculate_area_of_circle(square,5,3.14)
# Did NOt send square function as square() because if send as square(), result of square() pass function as parameter
# Function itself pass as parameter
print(f"Result of calculation is",result)

result = calculate_area_of_circle(square,4,3.14)
print(f"Result of calculation is",result)

result = calculate_area_of_circle(square,5,3)
print(f"Result of calculation is",result)

result = calculate_area_of_circle(square,4,3)
print(f"Result of calculation is",result)
