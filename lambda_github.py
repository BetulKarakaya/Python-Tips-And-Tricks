
# #https://docs.python.org/3/reference/expressions.html#lambda

# -->lambda_expr ::=  "lambda" [parameter_list] ":" expression"<--
# Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. 
#The expression lambda parameters: expression yields a function object. Quote from https://docs.python.org/3/reference/expressions.html#lambda


calculate_area_of_circle = lambda r: r * r * 3.14 

print(calculate_area_of_circle(5))
print(calculate_area_of_circle(12))


# map , filter etc. are built-in function 
#https://docs.python.org/3/library/functions.html You can get detailed information by checking this documentation.
#map() function -> https://docs.python.org/3/library/functions.html#map
#filter() function -> https://docs.python.org/3/library/functions.html#filter
print()

radius = [3,5,6,7,12,6,11,13,9,7,2,3]

calculeted_list = list(map(lambda r: r * r * 3.14 ,radius))
print("Calculated list of radius\n",calculeted_list)

print()

odd_numbers = list(filter(lambda x : x %2 == 1,radius))
odd_numbers_list = list(map(lambda r: r * r *3.14 , odd_numbers))
for i in range(len(odd_numbers)):
	print("{}. odd number -> {}. And calculated areacof circle is {}.".format(i+1,odd_numbers[i], odd_numbers_list[i]))

print()

even_numbers = list(filter(lambda x : x %2 == 0,radius))
even_numbers_list = list(map(lambda r: r * r *3.14 ,even_numbers))
for i in range(len(even_numbers)):
	print("{}. even number -> {}. And calculated areacof circle is {}.".format(i+1,even_numbers[i], even_numbers_list[i]))

print()

calculated_something = lambda x,y: x*y

print(calculated_something(3,4))

print()

def calculated_something_2(num):

	x = lambda num: (num * num * 7 )+30
	return x(num) + 17

print(calculated_something_2(1))
print(calculated_something_2(2))


# You can also use lambda functions with the pandas library. 
# Before trying this, please check if the pandas library is installed on your computer or you can use a suitable online environment.
#https://pandas.pydata.org/docs/getting_started/install.html
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html