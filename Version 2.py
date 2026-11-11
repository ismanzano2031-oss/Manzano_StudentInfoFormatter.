name1 = input("Enter first Name: ")
name2 = input("Enter last Name: ")
section = input("Enter section: ")
subject = input("Enter favorite Subject: ")

full_name = name1 + " " + name2
print("\nFormatted Output: ")
print(f"Name: {full_name.title()}")
print(f'Name Code: {full_name.upper()}')
print(f"Section: {section.upper()}")
print(f"Favorite Subject: {subject.title()}")
print(f"Character Count: {len(full_name)}")
