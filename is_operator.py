
def main():
    """
    None is a singleton object: only one instance of it can ever exist. So objects
    referencing None will always have the same identity. Same applies to True and False.
    """
    print("the is and is not operator test for an object's identity")
    print("the id() of None is")
    print(id(None))
    x = None
    y = None
    print("the id() of x is")
    print(id(x))
    print("the id() of y is")
    print(id(y))

    print("don't use '==' to compare a variable with None")


main()
