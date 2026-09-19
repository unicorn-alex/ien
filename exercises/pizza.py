import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv[1]) <= 4 or sys.argv[1][-4:] != ".csv":
    sys.exit("Not a Python file")
try:
    with open(sys.argv[1]) as file:
        rows = csv.reader(file)
        print(tabulate(rows, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
