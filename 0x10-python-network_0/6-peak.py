#!/usr/bin/python3
"""" Find peaks """""
def find_peak(list_of_integers):
    peaks = []
    if not list_of_integers:
        return []
    n = len(list_of_integers)
    if n == 1 or arr[0] >= arr[1]:
        peaks.append(0)

    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            peaks.append(i)

    if arr[-1] >= arr[-2]:
        peaks.append(n - 1)

    return peaks
