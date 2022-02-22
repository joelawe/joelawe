count = 0
tot = 0

while True:
    number = input("Enter a number")
    if number == 'done':
        break
    try:
        num1 = float(number)
    except:
        print("Invalid input")
        continue
    count = count + 1
    tot = tot + num1
print("All done")
print(tot, count, tot/count)
