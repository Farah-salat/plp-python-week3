count = 1
total = 0

# BUG: Missing colon at the end of the while loop header; added ':' to fix syntax error.
# BUG: Off-by-one condition 'count < 5' stopped at 4; changed to 'count <= 5' so 5 is included.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Concatenating string and integer 'total' raises TypeError; converted total using str(total).
print("Sum of 1 to 5 is: " + str(total))
