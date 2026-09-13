def logger(func):
    def wrapper():
        print("Function started")
        
        func()
        print("Function ended")
    return wrapper
@logger  #welcome = logger(welcome)
def welcome():
    print("Welcome to python")
welcome()


# Closer func
def create_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier
double = create_multiplier(2) #double is a function that multiplies its input by 2. and is any name
print(double(10))  # Output: 20
print(double(20))   # Output: 40