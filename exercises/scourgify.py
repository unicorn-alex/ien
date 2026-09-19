import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
try:
    with open(sys.argv[1], "r") as file1:
        students = list(csv.DictReader(file1))
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
with open(sys.argv[2], "w") as file2:
    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        name = student["name"].split(", ")
        writer.writerow({
            "first": name[1], "last": name[0], "house": student["house"]
            })
