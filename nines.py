# def nineSort(arr):
    # isNine = lambda x : x == 9
    # return sorted(arr, key = isNine)

# nineSort(nine)

def sort9(some_list):
    return filter(lambda x: x != 9, some_list) + filter(lambda x: x == 9, some_list)

sort9()
