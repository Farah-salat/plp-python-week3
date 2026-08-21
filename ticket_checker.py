age = int(input("Enter your age: "))

is_adult = age >= 18

print(f"Adult status: {is_adult}")

if is_adult:
    print("Adult ticket price: $10")
else:
    print("Child ticket price: $5")
