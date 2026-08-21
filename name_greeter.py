full_name = input("Enter your full name: ")

name_parts = full_name.split()

if len(name_parts) >= 2:
    first_name = name_parts[0]
    print(f"Hello, {first_name}!")
else:
    print("Please enter your full name.")
