class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # check whether my list array is full, if so, we will resize
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n # not using append because we already have empty space in array
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size] # return back the rightmost element present in the array

    def resize(self) -> None:
        self.capacity *= 2
        tempArray = [0] * self.capacity
        for i in range(self.size):
            tempArray[i] = self.array[i]
        self.array = tempArray

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity