import re
import phingImConvert

with open("TaigiDatabase.csv", "r") as f:
    lines = f.readlines()[1:] # skip the header

phingIm = set()
for line in lines:
    p = line.split(",")[1]
    p = p.strip("\n")

    p = p.replace("--", "@@ ")

    #we split at space (don't keep it) or after "-" (keep it) using regex
    p = re.split(" |(?<=-)", p)
    p = [x.replace("@@", "--") for x in p if x != ""]
    while "--" in p:
        index = p.index("--")
        p[index:index+2] = ["".join(p[index:index+2])]
    phingIm.update(p)

phingIm = list(phingIm)
phingIm = ["".join(phingImConvert.PhingImtoNUM(p)) for p in phingIm]
phingIm = sorted(phingIm)

incompletePhingIm = set()
for p in phingIm:
    for i in range(1, len(p)+1):
        incompletePhingIm.add(p[:i])

incompletePhingIm = sorted(list(incompletePhingIm))
incompletePhingIm = [p for p in incompletePhingIm if p not in ["-", "--"]]

with open("allPhingIm.txt", "w") as f:
    for p in phingIm:
        f.write(p)
        f.write("\n")

with open("incompletePhingIm.txt", "w") as f:
    for p in incompletePhingIm:
        f.write(p)
        f.write("\n")