class Level:
    def __init__(self, value=0):
        self.value = value
        print(f"The current value is: {self.value}")
    
    def __call__(self, x):
        self.value += x
        print(f"Value modified: the current value is {self.value}")


pipo = Level(3)
# pipo = 'hi' # not callable

# You can apply parenthesis '()' on a callable object: this invokes the __call__ method on that object.
if(callable(pipo)):
    print("pipo is callable")
    pipo(6)
    pipo(-1)
    pipo(-3.2)
else:
    print("pipo is not callable")
