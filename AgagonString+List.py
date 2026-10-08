fileName = input("Enter the file name: ")
lines = open(fileName)
count = 0

for line in lines:
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")