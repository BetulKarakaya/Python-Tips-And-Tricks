#It allows us to run an inner function defined inside the outer function after the outer function has finished running.
#They help us write code without using global value.


#Calculation of the area of the circle
def classic_outer_func(radius):
	pi = 3.14

	def classic_inner_func():

		print(pi * radius * radius)

	return classic_inner_func()

print("classic method\n")
classic_outer_func(2)


def closure_outer_func(p):
	pi = p

	def closure_inner_func(radius):

		print(pi * radius * radius)

	return closure_inner_func

my_func = closure_outer_func(3.14)

print("\nclosures\n")
print(my_func.__name__)
my_func(5) # 3.14 * 5 * 5 = 78.5
my_func(4) # 3.14 *4 *4 = 50.24
my_func = closure_outer_func(3)
my_func(5) # 3 * 5 * 5 = 75
my_func(4) # 3 * 4 * 4 = 48
