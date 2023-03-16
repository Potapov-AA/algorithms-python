from  multipledispatch import dispatch



class BubbleSort:
    @dispatch(list)
    def bubble_sort(arr):
        for i in range(0, len(arr)):
            for j in range(0, len(arr) - i):
                if(arr[j + 1] < arr[j]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr