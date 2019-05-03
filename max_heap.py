import math


class MaxHeap:
    def __init__(self, arr):
        self.array = arr
        self.size = len(arr)

    def buildheap(self):
        for i in range(math.floor(len(self.array)/2) - 1, -1, -1):
            k = i
            v = self.array[k]
            heap = False
            while not heap and (2 * k) + 1 <= len(self.array) - 1:
                j = (2 * k) + 1
                if j < len(self.array) - 1:
                    if self.array[j] < self.array[j+1]:
                        j = j + 1
                if v >= self.array[j]:
                    heap = True
                else:
                    self.array[k] = self.array[j]
                    k = j
            self.array[k] = v

    def heapify(self, i):
        largest = i
        l = 2 * i + 1  # left child
        r = 2 * i + 2  # right child

        if l < self.size and self.array[i] < self.array[l]:
            largest = l

        if r < self.size and self.array[largest] < self.array[r]:
            largest = r

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]  # swap
            self.heapify(largest)

    def deletemax(self):
        self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
        self.size -= 1
        self.heapify(0)
