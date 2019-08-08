# (*args) puts the arguments given into a list
def print2(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

def print2again(arg1,arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

def print1(arg1):
	print(f"arg1: {arg1}")

def print0():
	print("haha, it's empty")


print2("pupi", "pippi")
print2again("gnagno", "gnogno")
print1("pippi")
print0()