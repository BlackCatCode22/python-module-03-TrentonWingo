def find_min_max():
    numbers = []
    while True:
        try:
            num_str = input("Enter a number (or 'done' to finish): ")
            if num_str == 'done':
                break
            num = float(num_str)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    if numbers:
        print(f"Maximum: {max(numbers)}")
        print(f"Minimum: {min(numbers)}")
    else:
        print("No numbers entered.")


if __name__ == "__main__":
    find_min_max()