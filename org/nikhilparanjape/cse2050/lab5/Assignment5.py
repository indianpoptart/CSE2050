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

    def keys(self):
        temp_array = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                temp_array.append(self.map[i][0])
        return temp_array


if __name__ == '__main__':
    credentials = HashMap()
    credentials.add("password", "nikhilparanjape")
    credentials.add("admin", "johndoe")
    credentials.add("3ds87378fhH#&*hf783", "jeffbezos")
    credentials.add("83whf98h(#&*Hf78hjf73", "tonystark")
    credentials.add("thinkdifferent", "stevejobs")
    credentials.add("348h9zdontbeev89730wav87nwa9rv8n7a98wvril3uihf893", "sundarpichai")
    for key in credentials.keys():
        if credentials.get_hash(key) < 500:
            print("Username", credentials.get(key))


