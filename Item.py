class Item:
    def __init__(self, v, w, i):
        self.value = v
        self.weight = w
        self.index = i
        self.ratio = v/w

    def __lt__(self, other):
        return self.ratio < other.ratio

    def __le__(self, other):
        return self.ratio <= other.ratio

    def __gt__(self, other):
        return self.ratio > other.ratio

    def __ge__(self, other):
        return self.ratio >= other.ratio

    def __eq__(self, other):
        return self.ratio == other.ratio
# item_1 = Item(12, 2, 1)

# print(item_1.value)
# print(item_1.weight)
# print(item_1.ratio)
# print(item_1.index)
