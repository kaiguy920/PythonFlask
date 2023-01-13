# def named(**kwargs):
#     print(kwargs)

# named(name="bob", age=25)

# def named(name, age):
def named(**kwargs):
    print("kwargs in named function", kwargs)
# details = {'name': 'Bob', 'age': 25}
# named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="bob", age=25)