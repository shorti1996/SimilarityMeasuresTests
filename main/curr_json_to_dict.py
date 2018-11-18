import json
import re


currs = open("json_currencies.txt")
text = currs.read()

d = json.loads(text)

res = {}
for l in d:
    if len(l) == 6:  # whole line
        res[l[0]] = {l[1]: {"symbol": l[2], "ISO": l[3], "fractional": l[4], "base": l[5]}}
    elif len(l) == 5:  # country name absent
        res[list(res.keys())[-1]][l[0]] = {"symbol": l[1], "ISO": l[2], "fractional": l[3], "base": l[4]}
    else:
        print(len(l))
        raise Exception

res_str = json.dumps(res)

res_str = re.sub(r"\[.+?\]", "", res_str)
res_str = re.sub(r"\\t", "", res_str)
res_str = re.sub(r"\"\s+?(?=\w)", "\"", res_str)

x = 0
