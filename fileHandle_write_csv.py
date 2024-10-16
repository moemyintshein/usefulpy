import csv
name = input("Enter the name: ")
dob = input("Enter DOB (YYYY-MM-DD): ")
nrc = input("Enter NRC: ")
email = input("Enter email: ")
with open("data.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([name, dob, nrc, email])