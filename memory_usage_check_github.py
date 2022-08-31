import sys
import tracemalloc


#The sys.getsizeof statement gives information about how much memory the variable occupies.
#You can check this link for more detailed information.    https://docs.python.org/3/library/sys.html

num1 = 15
num2 = 155555

print("Memory usage of {var:s}".format(var="num1"),sys.getsizeof(num1))
print("Memory usage of {var:s}".format(var="num2"),sys.getsizeof(num2))


string1 = "15"
string2 = "155555"

print("Memory usage of {var:s}".format(var="string1"),sys.getsizeof(string1))
print("Memory usage of {var:s}".format(var="string2"),sys.getsizeof(string2))


list1 = [1,2,3,4]
list2 = [1,2,3,4,5,6,7,8]

print("Memory usage of {var:s}".format(var="list1"),sys.getsizeof(list1))
print("Memory usage of {var:s}".format(var="list2"),sys.getsizeof(list2))


#By using the tracemalloc library as follows, you can easily learn the memory usage of your functions and perform your optimization processes.
#The get_trace_memory() statement returns the memory value of the function as (current,peak).

#You can check this link for more detailed information.    https://docs.python.org/3/library/tracemalloc.html

def func_test1():
    tracemalloc.start()
    for i in range(10):
    	test_var = i

    result = tracemalloc.get_traced_memory()
    print("Current Memory usage of {var:s}".format(var="func_test1"), result[0])
    print("Max Memory usage of {var:s}".format(var="func_test1"), result[1])

    tracemalloc.stop()

def func_test2():
    tracemalloc.start()
    test_var = []

    for i in range(10):
    	test_var.append(i)

    result = tracemalloc. get_traced_memory()
    print("Current Memory usage of {var:s}".format(var="func_test2"), result[0])
    print("Max Memory usage of {var:s}".format(var="func_test2"), result[1])
    
    tracemalloc.stop()


func_test1()
func_test2()