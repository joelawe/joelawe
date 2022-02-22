largest = None
smallest = None

while True:
    number = input("Enter a number:")
    if number == 'done' or number == "Done":
        break
    try:
        number = float(number)
        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number
    except:
        print("Invalid input")
        continue
print(largest, smallest)
