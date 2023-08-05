a = int("Enter a sum: ")
b = int("Enter the currency your sum is in - choose 1 for $, 2 for € or 3 for ¥: ")
if b == 1:
    c = int("Enter the currency you want to transfer to: ")
    if c == 2:
        print(a * 0.91, "€")
    else:
        print(a * 141.75, "¥")
elif b == 2:
    c = int("Enter the currency you want to transfer to: ")
    if c == 1:
        print(a * 1.1, "$")
    else:
        print(a * 156.31, "¥")
else:
    c = int("Enter the currency you want to transfer to: ")
    if c == 1:
        print(a / 141.76, "$")
    else:
        print(a / 156.31, "€")