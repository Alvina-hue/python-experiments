
name = ["Anu", "Minu", "Sanu", "Jinu"]

print("Names of students:", name)

# Search student
search = input("Enter student name to search: ")

if search in name:
    print(search, "is found.")
else:
    print(search, "is not found.")

# Update student name
old_name = input("Enter old name to update: ")

if old_name in name:
    new_name = input("Enter new name: ")
    index = name.index(old_name)
    name[index] = new_name

    print("Updated names:", name)
    print("Student name updated successfully.")
else:
    print(old_name, "is not found in the list.")

# Remove a name
name.remove("Minu")

print("After removal:", name)

# Sort names
name.sort()

print("Sorted names:", name)

# Convert names to uppercase
upper_names = [name.upper() for name in name]

print("Uppercase names:", upper_names)

# Filter names starting with A
filter_names = list(filter(lambda name: name.startswith("A"), name))

print("Names starting with 'A':", filter_names)

