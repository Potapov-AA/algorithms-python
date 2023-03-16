from bubbleSort import BubbleSort


def test_bubble_sort_standart_array():
    arr = [9, 7, 5, 4, 3, 2, 1]
    assert BubbleSort.bubble_sort(arr) == [1, 2, 3, 4, 5, 7, 9]