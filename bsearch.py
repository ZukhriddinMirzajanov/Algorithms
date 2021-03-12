def bs(array, number):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right)/2)
        if number == array[mid]:
            return number
        elif number < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 'The number is not exist inside the array'


array = [3, 5, 7, 9, 12, 32, 45, 67, 89, 99]
print(bs(array, 909))
