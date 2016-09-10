#!/usr/bin/env python

import yaml

with open("../_data/team.yml") as f:
    team = yaml.load(f)

for mate in team:
    fname = mate["key"] + ".md"
    with open(fname, "w") as f:
        f.write("---\n")
        f.write("layout: team_member\n")
        for k,v in sorted(mate.items()):
            f.write("{}: {}\n".format(k, v))
        f.write("---\n")
        f.write("\n")
