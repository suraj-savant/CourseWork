import csv

def read_csv():
    with open("./tw5/data.csv", "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        return data

#  read data
data = read_csv()
for row in data:
    print(row)


#  create specific hypothesis
hypothesis = ['0' for _ in range(len(data[0])-1)]
print(f"\nInitial hypothesis : \n{hypothesis}")


# iterate through the data to change hypothsis
for row in data:
    print(f"\nFor the row {row}")
    if row[-1] == "No":
        print("Result is false so no change in hypothesis", hypothesis)
        continue

    # Change the hypotheis
    for i in range(len(row)-1):
        if hypothesis[i] == '0':
            hypothesis[i] = row[i]
        if hypothesis[i] != row[i]:
            hypothesis[i] = '?'
    print("The outcome is yes so change in hypothesis", hypothesis)


