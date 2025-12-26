from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        arr = data.copy()
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_array(self, array):
        return self.strategy.sort(array)

if __name__ == '__main__':
    # проверяем, что алгоритмы взаимозаменяемы
    array = [5, 3, 8, 4, 2]
    sorter = Sorter(BubbleSortStrategy())
    print("Bubble sort result:", sorter.sort_array(array))

    sorter.set_strategy(QuickSortStrategy())
    print("Quick sort result:", sorter.sort_array(array))

