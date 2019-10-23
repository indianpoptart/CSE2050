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
        ndx = self._findPosition(key)
        return ndx is not None

    def __iter__(self):
        return iter(self._entryList)

    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None

    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "invalid map key."
        self._entryList.pop(ndx)

    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        return self._entryList[ndx].value


# Question A
myMap = Map()
myMap.add(1, "A")
myMap.add(2, "D")
myMap.add(3, "E")
myMap.add(4, "B")
myMap.add(5, "A")
myMap.add(6, "N")

for i in range(len(myMap)):
    print(myMap._entryList[i].value)

# Question B
print('\nQuestion B:The Value for element 3 is:', end="\n")
print(myMap.valueOf(3))

# Question C
print('\nQuestion C:The second value was removed, now the list is:')
for i in range(len(myMap)):
    print(myMap._entryList[i].value)

# Question D
print('\nThe length of the list is:\n', len(myMap))