
# Nikhil Paranjape
# CSE 2050
# October 19 2019


class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self .value = value


class Map:

    def __init__(self):
        self._entryList = []

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, item):
        index = self._findPosition(item)
        return index is not None

    def _findPosition(self, item):
        for i in range(len(self)):
            if self._entryList[i].item == item:
                return i
            return None

    def add(self, key, value):
        index = self._findPosition(key)
        if index is not None:
            self._entryList[index].value = value
            return False
        else:
            entry = MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def remove(self, key):
        index = self._findPosition(key)
        assert index is not None, "Invalid map key."
        self._entryList.pop(index)

    def valueOf(self, key):
        index = self._findPosition(key)
        assert index is not None, "Invalid map key."
        return self._entryList[index].value


if __name__ == '__main__':
    print("Begin Assignment 4")
    myMap = Map()
    myMap.add(1, "A")
    myMap.add(2, "D")
    myMap.add(3, "E")
    myMap.add(4, "B")
    myMap.add(5, "A")
    myMap.add(6, "N")

    #print("b. " + myMap.valueOf(3))
    #myMap.remove(2)


