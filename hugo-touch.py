#!/usr/bin/env python3
# spec: https://rpeshkov.net/blog/update-timestamp-hugo-post/

import sys
from datetime import datetime

if len(sys.argv) < 2:
    print('Please provide filename')
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

found = False
outlines = []

now_date = ''

for line in lines:
    if not found and line.startswith('date'):
        now_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        line = 'date: ' + now_date + '\n'
        found = True

    outlines.append(line)

if not found:
    print('Date was not found in file!')
    sys.exit(1)

with open(sys.argv[1], 'w') as f:
    f.writelines(outlines)

print('Date updated to ' + now_date)