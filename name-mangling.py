class Backpack:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add(self, item):
        self.__items.append(item)

    def pop(self, item):
        # for i in range(len(self.__items)):
        #     if self.__items[i] == item:
        #         return self.__items[i]

        if item in self.__items:
            self.__items.remove(item)
            return True

        return False


mybackpack = Backpack()

mybackpack.add("laptop")
mybackpack.add("phone")
mybackpack.add("book")

# non-public attributes are not meant to be accessde directly
print(mybackpack._Backpack__items)

print("success") if mybackpack.pop("apple") else print("error findind apple in items")

# sorted returns a new list without modifying the original one
print(sorted(mybackpack.items))
