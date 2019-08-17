''' Symbol review '''


# assert
def my_assert():
    value = 12
    treshold = 10
    assert value <= treshold, "Value > treshold not allowed: {} > {}".format(value, treshold)

    print(isinstance(value, int))

def my_excepion():
    print("Exception management starts...")
    try:
        number = int(input('input an integer: \n> '))
        print('Your number is: {}'.format(number))
    except ValueError:
        print("Input value ain't no number")
    finally:
        print("Exception management finished.")

    # raise: forcefully raise exception: to be used only with custom exceptions

def my_lambda():
    value = 3
    squareit = lambda x : x * x
    print("squareit of {} is: {}".format(value, squareit(value)))

    a = 3
    b = 5
    sumem = lambda x,y : x + y
    print("squareit of {} is: {}".format(value, sumem(a,b)))


def main():
    # my_excepion()
    my_lambda()
    


if __name__ == "__main__":
    main()