import glob
import json, pprint

pp = pprint.PrettyPrinter(indent=4)


files = (glob.glob("/Users/fernb0t/code/d3proj/searchAlch/Search-Alchemy/personalities/*json"))

import csv

with open('combined.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["date", "Adventurousness", "Artistry", "Emotionality", "Imagination", "Curiosity", "Openess"])

    for fname in files:
        row = []
        row.append(fname.split("/")[-1].split(" ")[0])

        tree = json.load(open(fname))['tree']["children"]
        
        for branches in tree:
            for branch in branches["children"]:
                for leaf in branch["children"]:
                    if leaf['name'] == "Openness":
                        #pp.pprint(leaf["children"])
                        for personality in leaf["children"]:
                            row.append(personality['percentage'])
        writer.writerow(row)
