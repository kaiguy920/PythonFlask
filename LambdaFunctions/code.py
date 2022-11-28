# def add(x, y):
#     return x + y

# rewritten as lambda
#short functions meant to be used without a given name & used in conjunction with another function
#can be given a name, as shown below
# //////// with name /////////
# add = lambda x, y: x + y
# print(add(5,7))
# //////// without name /////////
#can get confusing this way, better to use a name if used solo & not in conjunction to another function
print((lambda x, y: x + y)(5, 7))

# def double(x):
#     return x * 2

sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence]
# same as above with lambda function
doubled = list(map(lambda x: x*2, sequence))
print(doubled)