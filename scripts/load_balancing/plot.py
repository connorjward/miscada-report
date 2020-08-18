# import pandas as pd
import re

with open("2pp_statistics") as f:
    match = re.findall("# \d+: (.*)", f.read())
    
print(match)

