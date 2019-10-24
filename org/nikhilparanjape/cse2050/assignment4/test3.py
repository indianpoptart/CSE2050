# Nikhil Paranjape
# CSE 2050
# October 19 2019


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Map:

    def __init__(self):
        self._entryList = []

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        index = self._findposition(key)
        return index is not None

    def __iter__(self):
        return iter(self._entryList)

    def _findposition(self, item):
        for i in range(len(self)):
            if self._entryList[i].key == item:
                return i
        return None

    def add(self, key, value):
        index = self._findposition(key)
        if index is not None:
            self._entryList[index].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def remove(self, key):
        index = self._findposition(key)
        assert index is not None, "Invalid map key."
        self._entryList.pop(index)

    def valueOf(self, key):
        index = self._findposition(key)
        assert index is not None, "Invalid map key."
        return self._entryList[index].value

    def printmap(self):
        for temp in range(len(myMap)):
            print(self._entryList[temp].value)


if __name__ == '__main__':
    print("Begin Assignment 4: Maps")
    print(34 * "-", "\n1a. Add function with key-value pairs \n", 33 * "-")
    myMap = Map()
    myMap.add(1, "A")
    myMap.add(2, "D")
    myMap.add(3, "E")
    myMap.add(4, "B")
    myMap.add(5, "A")
    myMap.add(6, "N")
    
    myMap.printmap()

    print(30 * "-", "\n1b. Search for value of key 3\n", 29 * "-")
    print('The Value for element 3 is: \n', myMap.valueOf(3))

    print(34 * "-", "\n1c. Remove element '2' Printed map:\n", 33 * "-")
    myMap.remove(2)
    myMap.printmap()

    print(34 * "-", "\n1d. Printing length of list of pairs \n", 33 * "-")
    print("The length of the list is:\n", len(myMap))
