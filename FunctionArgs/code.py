# * allows for any arg type & amount into one parameter
def multiply(*args):
    # print(args) #=> typle
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 3, 5))

# ============================================================================
# can also use * to destructure an argument into multiple parameters
def add(x, y):
    return x + y
#  /// with list ///
nums = [3, 5]
print(add(*nums))

#  /// with dictionary ///
nums = {'x': 15, 'y': 25}
print(add(**nums))

# ============================================================================
def mult(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total

# collect all postiional arguments into tuple (args) & have named argument at the end
def apply(*args, operator):
    if operator == "*":
        return mult(*args)
    elif operator == "+":
        return sum(args)
    else: 
        return "no valid operator to apply()."

print("multiply and apply function", apply(1, 3, 6, 7, operator="*"))