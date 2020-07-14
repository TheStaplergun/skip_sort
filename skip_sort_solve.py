#!/usr/bin/env python3

import sys
path = str(sys.argv[1])
with open(path, "r") as f:
  data = f.readlines()
  pos = int(data[0]) - 1
  sortable_data = [x for x in data[1:]]
  sortable_data.sort(key=lambda e:([e[pos] for pos, char in enumerate(e) if pos%4 == 0]))
  for line in sortable_data:
    print(line[:-1])
