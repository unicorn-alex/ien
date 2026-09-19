import sys

nb_of_lines = 0
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv[1]) <= 3 or sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")
try:
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.strip()
            if line == "" or line[0] == '#':
                continue
            nb_of_lines += 1
except FileNotFoundError:
    sys.exit("File does not exist")
print(nb_of_lines)
