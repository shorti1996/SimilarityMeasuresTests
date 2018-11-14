from pyxdameraulevenshtein import damerau_levenshtein_distance_ndarray, normalized_damerau_levenshtein_distance_ndarray
import numpy as np
import nwalign


currs = open("currencies_ISO4217.txt")
curr_names = open("currencies_ISO4217_names.txt")

curr_signs_names = [line.strip() for line in open("currencies_signs_names.txt")]
curr_signs_names_arr = np.array(curr_signs_names)

curr_signs = open("currencies_signs.txt")

curr_dict = {}
for line in currs:
    name = curr_names.readline().strip()
    curr_dict[line.strip()] = name

signs_dict = {}
for line in curr_signs_names:
    signs_dict[line] = curr_signs.readline()

for key, value in curr_dict.items():
    dists = normalized_damerau_levenshtein_distance_ndarray(value, curr_signs_names_arr)
    best = np.argmin(dists)
    name = curr_signs_names[best]
    if value != name:
        x = 0

x = 0