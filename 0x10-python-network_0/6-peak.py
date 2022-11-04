#!/usr/bin/python3
"""Technical interview preparation:"""

def find_peak(list_of_integers):
    """ function that finds a peak in a list"""
    arr = sorted(list_of_integers)
    if list_of_integers == []:
        return None
    return(arr[-1])    

