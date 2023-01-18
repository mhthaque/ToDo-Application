def get_average():
    with open("numbers.txt", "r") as file:
        data = file.readlines()[1:]
        data = [float(item) for item in data]
        average_local = sum(data) / len(data)
    return average_local


average = get_average()
print(average)



