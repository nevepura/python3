def fill_numbers(numbers, quantity, increment):
    '''
    # while loop
    i = 0
    while i < quantity:
        print(f"At the top there is {i}")
        numbers.append(i)
        i += increment
        print(f"At the bottom there is {i}")
    print(f"numbers are: {numbers}")
    '''
    for i in range (0, quantity, increment):
        print(f"At the top there is {i}")
        numbers.append(i)
        print(f"At the bottom there is {i}")
    print(f"numbers are: {numbers}")


def main():
    numbers = []
    quantity = 10
    increment = 3
    fill_numbers(numbers, quantity, increment)

if __name__ == "__main__":
    main()

