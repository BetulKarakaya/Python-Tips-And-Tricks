#In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing
#the results of expensive function calls and returning the cached result when the same inputs occur again.
#YWikipedia, “Memoization”,https://en.wikipedia.org/wiki/Memoization#

def classic_fib(n):

    if n>0 and n<=2:
        return 1
    else:
        return classic_fib(n-2) + classic_fib(n-1)

#(it does not calculate bşg number quickly)
print("Classic fib function (3. step):", classic_fib(3))


def memoization_fib(n):

    if n<=2:
        return 1
    else:
        if not n in mem:
            mem[n]= memoization_fib(n-2) + memoization_fib(n-1)
        return mem[n]

mem = {} #Python dictionary
print("Fib function that use memoization in simple way (50. step):", memoization_fib(50))


memo = {}
def memoize_decorators(f): # f peresent function in this case it is fib_decorators
    def wrapper(*args):
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return wrapper  # return the wrapper to call wrapper otherwise wrapper does not run

@memoize_decorators # Every time fib_decorators func call the memoize_decorators call 

# ---> if you have any struggle to understand decorators you can research first-class function and closures first

def fib_decorators(n):

    if n <=2:
        return 1
    else:
        return fib_decorators(n-1) + fib_decorators(n-2)

print("Fib function that use memoization with decorators (50. step):", fib_decorators(50))



class Memoize_class:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]
@Memoize_class
def fib_class_decorators(n):
    if n<=2:
        return 1
    else:
        return fib_class_decorators(n-1) + fib_class_decorators(n-2)

print("Fib function that use deorators in class (50. step):",fib_class_decorators(50))