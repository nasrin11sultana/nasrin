lines = []

while True:
    line = input("Enter a line (or 'STOP' to end): ")
    if line.lower() == "stop":
        break
    lines.append(line.upper())

for line in lines:
    print(line)
