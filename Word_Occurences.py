file = open("Lorem Ipsum.txt", "r")
data = file.read()
data_list = data.split()

dict = {}
total_data = 0

for data in data_list:
    data = data.replace(".", "")
    data = data.replace(",", "")
    data = data.replace("\n", "")
    data = data.replace(" ", "")
    if data.lower() in dict:
        dict[data.lower()] += 1
    else:
        dict[data.lower()] = 1
    total_data += 1

print(dict)
print(total_data)