# ======================= STRING FORMATTING =======================
name = "Bob"
# greeting = f"Hello {name}"
greeting = "Hello {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

# print(greeting)
# print(with_name, with_name_two)

longer_phrase = "Hello {}. Today is {}"
formatted = longer_phrase.format("Rolf", "Monday")
# print(formatted)

# ======================= USER INPUT =======================
# name = input("Enter your name: ")
# input always returns a string
# print(name)

# math
size_input = input("How big is your hous (in sq ft): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is {square_meters:.2f} square meters")