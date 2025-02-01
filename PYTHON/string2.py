#!/usr/bin/python3

def frequence_str(string):
    freq_dict = {}
    for char in string:
        keys = freq_dict.keys()
        if char in keys:
            freq_dict[char] += 1
        else:
            freq_dict[char] =1
    return freq_dict
print(frequence_str('google.com'))


