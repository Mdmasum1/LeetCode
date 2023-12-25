
# Implementing a heap data structure that includes both min heap
# max heap, insert,, delete operations is a useful exercise. Below
# is a python implementation of a heap class that covers these aspects
# step by step


class Heap():

    def __init__(self, max_heap=True): #heap_type='min' or 'max
        self.heap = []  #intialize empty list to the heap
        #self.heap_type = heap_type #'min' for min heap, 'max' for max heap
        self.max_heap = max_heap


    def parent(self, i):
        return  (i - 1)// 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def compare(self, a, b):
        return a > b if self.max_heap else a < b

        
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    #Implementation of remove method
    def remove(self):
        #Base case
        if len(self.heap) == 0:
            return None
        #if heap is not none then remove element from the top
        if len(self.heap) == 1:
            return self.heap.pop()

        #Top element of heap store as max_value
        max_value = self.heap[0]
        
        if max_value == -1:
            return
        #Now, pop from end of the heap and store it to top of the heap
        self.heap[0] = self.heap.pop()
        #Re-arrange the heap by calling heapify_down method to maintain
        #the heap property
        self.heapify_down(0)

        return max_value



    def delete(self, value):
        if len(self.heap) == 0:
            return

        index = self.heap.index(value)
        if index == -1:
            return

        self.swap(index, len(self.heap) - 1)  # Fix here: Swap with len(self.heap) - 1
        self.heap.pop()
        self.heapify_down(index)

    def heapify_up(self, i):
        while i > 0 and self.compare(self.heap[i], self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)


    def heapify_down(self, i):
        while True:
            left = self.left_child(i)
            right = self.right_child(i)
            largest = i


            if (left < len(self.heap) and self.compare(self.heap[right], self.heap[largest])):

                largest = left

            if ( right < len(self. heap) and self.compare(self.heap[left], self.heap[largest])):
                largest = right

            if i != largest:
                self.swap(i, largest)
                i = largest

            else:
                break

    def extract_root(self):
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.heapify_down(0)

        return root

    def peek_root(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def display(self):
        print(self.heap)



# Example usage:
min_heap = Heap(max_heap=False)
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(2)
min_heap.insert(1)

min_heap.display()  # Output: [1, 2, 8, 5, 3]

min_heap.delete(5)
min_heap.display()  # Output: [1, 2, 8, 3]

print(min_heap.extract_root())  # Output: 1

max_heap = Heap(max_heap=True)
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(8)
max_heap.insert(2)
max_heap.insert(1)

max_heap.display()  # Output: [8, 5, 3, 2, 1]

max_heap.delete(5)
max_heap.display()  # Output: [8, 2, 3, 1]

print(max_heap.extract_root())  # Output: 8








