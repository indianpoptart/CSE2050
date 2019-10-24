class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Map:

    def __init__(self):
        self.entryList = []

    def __len__(self):
        return len(self.entryList)

    def __contains__(self, key):
        index = self._findposition(key)
        return index is not None

    def __iter__(self):
        return iter(self.entryList)

    def _findposition(self, item):
        for i in range(len(self)):
            if self.entryList[i].item == item:
                return i
        return None

    def add(self, key, value):
        index = self._findposition(key)
        if index is not None:
            self.entryList[index].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self.entryList.append(entry)
            return True

    def remove(self, key):
        index = self._findposition(key)
        assert index is not None, "Invalid map key."
        self.entryList.pop(index)

    def valueOf(self, key):
        index = self._findposition(key)
        assert index is not None, "Invalid map key."
        return self.entryList[index].value


print("Begin Assignment 4")
myMap = Map()
myMap.add(1, "A")
myMap.add(2, "D")
myMap.add(3, "E")
myMap.add(4, "B")
myMap.add(5, "A")
myMap.add(6, "N")

for i in range(len(myMap)):
    print(myMap.entryList[i].value)
