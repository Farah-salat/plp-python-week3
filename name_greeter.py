full_name = input("Enter your full name: ")

name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]

print(f"Hello, {first_name}!")
print(f"Your last name is {last_name}.")