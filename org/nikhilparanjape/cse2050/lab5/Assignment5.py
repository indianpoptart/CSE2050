# Hash Map


class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def get_hash(self, key):
        temp_hash = 0
        for char in str(key):
            temp_hash += ord(char)
        return temp_hash % self.size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print(30 * "-", '\nUserPassMap', 29 * "-")
        for item in self.map:
            if item is not None:
                print(str(item), end=" ")

    def ratelist(self, weight):
        pass


if __name__ == '__main__':
    credentials = HashMap()
    credentials.add("nikhilparanjape", "password")
    credentials.add("johndoe", "admin")
    for key, value in credentials.items():
        credentials.get_hash(key)
