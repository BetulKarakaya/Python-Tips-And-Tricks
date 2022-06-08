#Usually, First for loop that teach at college or courses are in this way. 
#First you define a bool value, then  inside a loop you update the value 
#and then you code  a if -else block to check result or do something according to result.

def classic_for_loop(test_list,num):

	find = False
	for item in test_list:

		if(item == num):
			find = True
			break;


	if(find):
 		print("FINDED",num)
	else:
 		print("NOT FINDED",num)

	

#This way can be difficult to read the code later. It is important to write readable code.
#Especially when you code long blocks of code, you want your code to conform to clean code standards.


#If the break command inside the "if block" is executed, the "else block" is not executed.
#However if the break command inside the "if block" is not executed, the "else block" is executed.

def for_else_loop(test_list,num):

	for item in test_list:

		if item == num:
			print("FINDED",num)
			break;  # DON'T FORGET BREAK COMMAND
	else:
		print("NOT FINDED",num)



test_list = [1,2,3,4,5,6,72,81]

classic_for_loop(test_list,6)
classic_for_loop(test_list,48)

for_else_loop(test_list,6)
for_else_loop(test_list,48)
