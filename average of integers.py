total = 0
count = 0

while True:
    user_input = input("Enter an integer or 'done': ")
    if user_input == "done":
        break
    try:
        number = int(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input")

if count > 0:
    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No valid numbers entered.")