# This program prints different number patterns
# User chooses which pattern and the height

# asking user for pattern choice
print("Choose a pattern:")
print("1. Increasing numbers")
print("2. Same number repeated")
print("3. Reverse decreasing")
print("4. Pyramid pattern")

pattern_choice = int(input("Enter pattern number (1-4): "))
pattern_height = int(input("Enter height: "))

print()  # empty line for spacing

# ===== Pattern 1 =====
# 1
# 1 2
# 1 2 3 ...
if pattern_choice == 1:
    for i in range(1, pattern_height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# ===== Pattern 2 =====
# 1
# 2 2
# 3 3 3 ...
elif pattern_choice == 2:
    for i in range(1, pattern_height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# ===== Pattern 3 =====
# 5 4 3 2 1
# 4 3 2 1 ...
elif pattern_choice == 3:
    for i in range(pattern_height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# ===== Pattern 4 =====
# 1
# 1 2 1
# 1 2 3 2 1 ...
elif pattern_choice == 4:
    for i in range(1, pattern_height + 1):
        # increasing part
        for j in range(1, i + 1):
            print(j, end="")
        # decreasing part
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

# invalid option
else:
    print("Invalid pattern choice")