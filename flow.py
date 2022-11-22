# ======================= BOOLEAN =======================
# Comparisons: ==, !=, >, <, >=, <=
# print(5 == 5) #true
# print(5 == "5") #false
# print(10 != 10) #false

# friends = ["Rolf", "Bob"]
# abroad = ["Rolf", "Bob"]
# print("==", friends == abroad) #true ** better/more relable way to compare **
# print("is", friends is abroad) #false

# ======================= IF STATEMENTS =======================
# day_of_week = input("What day of the week is it today? ").lower()
# print(day_of_week == "Monday")
# if day_of_week == "monday":
#     print("Have a great start to your week!")
# elif day_of_week == "tuesday":
#     print("It's Tuesday")
# else:
#     print("Full speed ahead")

# ======================= IN STATEMENTS =======================
amigos = ["Rolf", "Bob", "Jen"]
print("Jen" in amigos)#true

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")
print(user_movie in movies_watched)

# ======================= IF STATEMENTS W/ IN KEYWORD =======================
if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")

# //// ANOTHER EXAMPLE ////
number = 7
# user_input = input("Enter 'y' if you would like to play: ").lower()

# if user_input == "y":
#     user_number = int(input("Guess our number: "))
#     if user_number == number: 
#         print("You guessed correctly!")
#     # elif number - user_number in (1, -1):
#     elif abs(number - user_number) == 1:
#         print("You were off by one")
#     else:
#         print("sorry, it's wrong")

# ======================= LOOPS =======================
# //// WHILE LOOP ////
# user_input = input("Enter 'y' if you would like to play? (Y/n) ")

# while user_input != "n":
while True:
    user_input = input("Enter 'y' if you would like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number: 
        print("You guessed correctly!")
    # elif number - user_number in (1, -1):
    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("sorry, it's wrong")
    user_input = input("Enter 'y' if you would like to play? (Y/n) ")

# //// FOR LOOP ////
people = ["Rolf", "Jen", "Bob", "Anne"]

for friend in people:
# for friend in range(3):
    print(f"{friend} is my friend.")

# //// ANOTHER EXAMPLE ////
grades = [35, 67, 98, 100, 100]
total = 0
amount =len(grades)

for grade in grades:
    total += grade 

total2 = sum(grades)

print(total / amount)