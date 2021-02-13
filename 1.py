# 20 вариант
from random import randint
from array import array


def found_element(arr: array) -> int:
    size = len(arr)
    already_has = False  # Note if program found first positive digit
    min_positive_digit = 0

    for i in range(size):
        if arr[i] > 0 and not already_has:  # Check for availability of first positive digit
            min_positive_digit = arr[i]
            pos = i
            already_has = True
        elif arr[i] > 0 and already_has:  # Check if we have positive digit
            if arr[i] < min_positive_digit:
                min_positive_digit = arr[i]
                pos = i

    if min_positive_digit == 0:
        return -1
    else:
        return pos


def solution():
    numbers = array('i', [int(elem) for elem in input('Введите элементы через пробел: ').split()])

    print(f'Позиция минимального положительного числа: {found_element(numbers)}')


# n = int(input('Введите количество элементов в массиве:'))
# for i in range(n):
#    numbers.append(randint(-10, 10))

if __name__ == '__main__':
    solution()

# [-6, -7, 5, 1, -3, 8]
