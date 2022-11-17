class Backpack:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def pop(self, item):
        for i in range(len(self.__items)):
            if self.__items[i] == item:
                return self.__items[i]

        return None


mybackpack = Backpack()

mybackpack.add("laptop")
mybackpack.add("phone")
mybackpack.add("book")

# non-public attributes are not meant to be accessde directly
print(mybackpack._Backpack__items)

print(mybackpack.pop("apple"))
print(mybackpack.pop("laptop"))
