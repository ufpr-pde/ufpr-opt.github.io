#!/usr/bin/env python3

import datetime
import yaml

with open("events.yml", "r") as stream:
    data = yaml.load(stream)

today = datetime.date.today()
dates = []
for d in ['date', 'datesub']:
    for i in range(0, len(data)):
        if data[i][d] > today:
            if "acro" in data[i]:
                name = data[i]['acro']
            else:
                name = data[i]['name']
            dates.append( (data[i][d], name, d, data[i]['key']) )

with open("calendar.yml", "w") as f:
    f.write("# Generated automatically. Don't edit manually\n")
    f.write("# Last modified: {}\n".format(today))
    for d in sorted(dates):
        if d[2] == "date":
            what = "Start of "
        else:
            what = "Submission deadline of "
        f.write("- date: {}\n  name: {}\n  key: {}\n".format(d[0], what + d[1],
            d[3]))
