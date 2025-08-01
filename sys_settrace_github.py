import sys

class Debugger:
    def __init__(self):
        pass
    
    def trace_func(self,frame, event, arg):
        if event == "call":
            print(f"\n- Calling: {frame.f_code.co_name}()")
        elif event == "line":
            print(f"-- Line {frame.f_lineno} in {frame.f_code.co_name}")
        elif event == "return":
            print(f"- Returning from: {frame.f_code.co_name}() with value: {arg}")
        return self.trace_func

    def add(self,x, y):
        z = x + y
        return z

    def multiply(self,a, b):
        result = self.add(a, b)
        return result * 2

def main():
    debugger = Debugger()
    sys.settrace(debugger.trace_func)
    debugger.multiply(3, 4)
    sys.settrace(None)

if __name__ == "__main__":
    main()