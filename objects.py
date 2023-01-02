def main():

    print("everything in Python is an object!")
    print("is 5 an instance of object?")
    print(isinstance(5,object))

    print("is False an instance of object?")
    print(isinstance(False, object))

    print("is f(x) an object?")
    print(isinstance(f, object))


def f(x):
    return x * x


if __name__ == "__main__":
    main()

