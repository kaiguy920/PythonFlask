# ======================= LIST COMPREHENSIONS =======================

numbers = [1, 3, 5]
# doubled = []
doubled = [x * 2 for x in numbers]

# for num in numbers:
    # doubled.append(num * 2)

# print(doubled)

# //////////////////////////////////////////////////////////////////////
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
# print(starts_s)

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

# ======================= DICTIONARIES =======================
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
# have to access value with key, not index
friend_ages["Bob"] = 20
# print(friend_ages["Adam"])
# print(friend_ages)
# //////////////////////////////////////////////////////////////////////
amigos = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]
#can access single dictionary in a list with index
# print(amigos[0]["name"])
# //////////////////////////////////////////////////////////////////////
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print("List", list(student_attendance.items()))

# tuple 
# for t in student_attendance.items():
#     print("tuple", t)

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}%")

#can only check key
# if "Bob" in student_attendance:
#     print(f"Bob: {student_attendance['Bob']}")
# else: 
#     print("Bob is not a student in this class")

# attendance_values = student_attendance.values()
# print("values", attendance_values)
# print(sum(attendance_values) / len(attendance_values))

# ======================= DESTRUCTURING VARIABLES =======================
# ** WAY 1 **
# x = 5
# y  = 11
# ** WAY 2 **
# x, y = 5, 11
# ** WAY 3 **
t = 5, 11
x, y = t
# print(x, y) # => 5, 11

# //////////////////////////////////////////////////////////////////////

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("harry", 32, "Lecturer")]

# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")

# for person in people:
    # print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

# person = ("Bob", 42, "Mechanic")
# _ variable in Python will be ignored
# name, _, profession = person
# print(name, profession) # ==> Bob Mechanic

# //////////////////////////////////////////////////////////////////////
# * all of the rest, the following
# head, *tail = [1, 2, 3, 4, 5]
# print(head)
# print(tail)

# ======================= FUNCTIONS =======================
# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 *60
#     print(f"Your age in seconds is {age_seconds}.")

# print("Welcome to the age in seconds program!")
# user_age_in_seconds()
# print("Goodbye!")
# //////////////////////////////////////////////////////////////////////
 
def add(x,y):
    # result = x + y
    # print(result)
    return x + y

# add(5, 3)
result = add(5, 3)
print("add result", result)

# //////////////////////////////////////////////////////////////////////

def divide(dividend, divisor):
    if divisor != 0:
        # divide = dividend / divisor
        # print(f'{divide:.2f}')
        return dividend / divisor
    else:
        print("You fool!")
result = divide(15, 3)
print(result)
# divide(dividend=15, divisor=7)