# Nikhil Paranjape
# Updated v2


class GroceryList:

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


if __name__ == '__main__':
    print("Start Shopping")

    # Set initial total cost to $0
    totalcost = 0
    # Create a rate list with prices for each item
    ratelist = {'apple': 35, 'grapes': 21, 'melon': 10, 'blueberry': 9, 'orange': 12, 'raspberry': 8}

    # Create basic shop list
    shop = GroceryList()

    # Add fruit and weight of item
    shop.add("apple", 3.5)
    shop.add("orange", 2.3)
    shop.add("blueberry", 2.5)
    shop.add("raspberry", 3)
    shop.add("grapes", 1.5)
    shop.add("melon", 10)

    # Iterate through the list of rates
    # Multiply the amount of produce and the rate for that produce
    for key in list(ratelist.keys()):
        totalcost += (ratelist.get(key)) * (shop.get(key))

    print(30 * "-")

    # Show what we are buying
    print("We are buying:")
    for key in list(ratelist.keys()):
        print(key, shop.get(key),"lbs", "@ $", ratelist.get(key))

    print(30 * "-")
    print("The total cost of the shopping list is: $", totalcost)
