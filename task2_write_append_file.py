user_input = input("Enter a value: ")

with open("output.txt", "w") as file:
    file.write(f"User entered: {user_input}\n")

with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

print("\nFinal content of the file:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
