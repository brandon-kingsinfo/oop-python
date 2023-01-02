def main():
    """
    The current implementation keeps an array of integer objects for all
    integers between -5 and 256. When you create an int in that range
    you actually just get back a reference to the existing object.

    IDEs like PyCharm and VS Code will perform some memory optimizations,
    so 'c is d' will return True, but in IDLE it will return False when
    these statements are not inside a function
    """
    a = 255
    b = 255
    print("if a is b?")
    print(a is b)
    c = 1566
    d = 1566
    print("if c is d?")
    print(c is d)
    print(id(c))
    print(id(d))


main()


