#!/usr/bin/python3

def find_peak(list_of_integers):
    list_start = 0
    list_len = len(list_of_integers)
    list_end = list_len - 1

    if list_len < 1:
        return None

    while list_start < list_end:
        mid = (list_start + list_end) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            list_start = mid + 1
        else:
            list_end = mid

    return list_of_integers[list_start]
