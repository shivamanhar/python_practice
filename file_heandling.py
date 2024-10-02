#two method for file read

with open("sample_text.txt") as file:
    for line in file:
        print(line, end=" ")


file_data = open("sample_text.txt")

for line in file_data:
    print(line, end='')
file_data.close()
