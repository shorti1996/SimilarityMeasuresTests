import numpy as np

import main.smithWaterman.smith_waterman2 as sw

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
    signs_dict[line] = curr_signs.readline().strip()

for key, value in curr_dict.items():
    dists = []
    for curr_name in curr_signs_names:
        i, j, score = sw.find_max(sw.scoring_matrix(value, curr_name))
        dists.append((score, curr_name))

    name = max(dists)[1]
    curr_dict[key] = {"name1": value, "name2": name, "sign": signs_dict[name]}
    if value != name:
        x = 0

x = 0