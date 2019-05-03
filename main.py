import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import time
from Item import Item
from max_heap import MaxHeap

def get_array(file):
    array = []
    for line in file:
        array.append(int(line))
    return array


def main():

    # array = [1, 5, 3, 6, 1, 2, 5, 7, 8, 10]
    # maxheap = MaxHeap(array)
    # maxheap.heapify()

    #plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'go')
    #plt.axis([0, 6, 0, 20])
    #plt.show()

    #x = np.linspace(0, 2, 100)

    #plt.plot(x, x, label='linear')
    #plt.plot(x, x ** 2, label='quadratic')
    #plt.plot(x, x ** 3, label='cubic')

    #plt.xlabel('x label')
    #plt.ylabel('y label')

    #plt.title("Simple Plot")

    #plt.legend()

    #plt.show()

    capacity_file = input("Enter file containing the capacity: ")  # p00_c.txt
    capacity_f = open(capacity_file, 'r')
    knapack_capacity = capacity_f.readline().rstrip()  # 5
    # print(knapack_capacity.read())

    weight_file = input("Enter file containing the weights: ")  # p00_w.txt
    weight_f = open(weight_file, 'r')  # 2, 1, 3, 2
    # print(weight.read())

    value_file = input("Enter file containing the values: ")  # p00_v.txt
    value_f = open(value_file, 'r')  # 12, 10, 20, 15
    # print(value.read())

    weight_array = get_array(weight_f)
    value_array = get_array(value_f)
    num_items = len(value_array)

    # close files
    capacity_f.close()
    weight_f.close()
    value_f.close()

    print("\nKnapsack capacity = " + str(knapack_capacity) + ". Total number of items = " + str(num_items))

    # Task 1a: Dynamic Programming (traditional) approach
    # Creates a table containing n = num_items, and weight W = knapsack capacity, all set to 0
    n, W = num_items, int(knapack_capacity)
    # table = [[0 for j in range(W+1)] for i in range(n+1)]
    # # table[4][5] = ex: 99  # goal
    #
    # # Compute values table(i,j) left to right row wise
    # dp_start = time.time()
    #
    # for i in range(1, n+1):
    #     for j in range(1, W+1):
    #         # print(str(i) + ", " + str(j))
    #         if j - weight_array[i-1] >= 0:
    #             table[i][j] = max(table[i-1][j], value_array[i-1] + table[i-1][j-weight_array[i-1]])
    #         elif j - weight_array[i-1] < 0:
    #             table[i][j] = table[i-1][j]
    #
    # remaining_weight = W
    # optimal_subset_dp = []
    # for i in range(n, 0, -1):
    #     # starting at table[n,W] and i = n first
    #     if table[i-1][remaining_weight] > (value_array[i-1] + table[i-1][remaining_weight - weight_array[i-1]]):
    #         # print("Item " + str(i) + " was not chosen!")
    #         pass
    #     elif (remaining_weight - weight_array[i-1]) < 0:
    #         # print("Item " + str(i) + " was not chosen!")
    #         pass
    #     else:
    #         # print("Item " + str(i) + " was chosen!")
    #         optimal_subset_dp.append(i)
    #         remaining_weight = remaining_weight - weight_array[i-1]
    #
    # dp_end = time.time()
    #
    # print("\nTraditional Dynamic Programming Optimal value: " + str(table[num_items][W]))
    # print("Traditional Dynamic Programming Optimal subset: {", end="")
    # print(*sorted(optimal_subset_dp), sep=", ", end='}')
    # print("\nTraditional Dynamic Programming Time Taken: " + str(dp_end - dp_start))

    # Task 2a: Greedy approach using in-built sort
    # arranges the items in the decreasing order of value to weight ratio (vi/wi for i = 1, 2, ..., n),
    # then select the items in this order until the weight of the next item exceeds the remaining capacity
    # (Note: In this greedy version, we stop right after the first item whose inclusion
    # would exceed the knapsack capacity).

    greedy_array = []
    optimal_subset_g = []

    g_start = time.time()  # start timer here?

    for i in range(1, num_items+1):
        greedy_array.append(Item(value_array[i-1], weight_array[i-1], i))

    heap_array = greedy_array.copy()  # for Task 2b!

    greedy_array.sort(reverse=True)
    total_weight = 0
    total_value = 0

    for i in range(num_items):
        if (total_weight + greedy_array[i].weight) > W:
            break
        else:
            optimal_subset_g.append(greedy_array[i].index)
            total_weight += greedy_array[i].weight
            total_value += greedy_array[i].value

    g_end = time.time()

    print("\nGreedy Approach Optimal value: " + str(total_value))
    print("Greedy Approach Optimal subset: {", end="")
    print(*sorted(optimal_subset_g), sep=", ", end='}')
    print("\nGreedy Approach Time Taken: " + str(g_end - g_start))

    # Task 2b: Greedy approach using max-heap
    # Implement the greedy algorithm based on a max-heap that supports the operations insert and delete max.
    # The idea is to use the O(n) algorithm (bottom-up approach) to build the heap containing
    # the n keys (vi/wi for i = 1, 2, ..., n) then perform a series of delete max.
    # If the number of objects that are selected by the greedy algorithm is k, then the total complexity is
    # O(n + k log n) which could be better than O(n log n) in some cases (the complexity of best sorting algorithm).

    # using heap_array from task 2a, should time include making the array of ratios?
    gheap_start = time.time()  # start timer here?

    maxheap = MaxHeap(heap_array)
    maxheap.buildheap()

    optimal_subset_gheap = []
    total_weight = 0
    total_value = 0

    heap_array_length = len(maxheap.array)

    for i in range(heap_array_length):
        if (total_weight + heap_array[0].weight) > W:
            break
        else:
            optimal_subset_gheap.append(heap_array[0].index)
            total_weight += heap_array[0].weight
            total_value += heap_array[0].value
            maxheap.deletemax()  # pop item, sifts in log

    gheap_end = time.time()

    print("\nHeap-based Greedy Approach Optimal value: " + str(total_value))
    print("Heap-based Greedy Approach Optimal subset: {", end="")
    print(*sorted(optimal_subset_gheap), sep=", ", end='}')
    print("\nHeap-based Greedy Approach Time Taken: " + str(gheap_end - gheap_start))
    print('\n')

main()
