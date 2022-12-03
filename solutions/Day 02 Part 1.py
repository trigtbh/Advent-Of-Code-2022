import helper
with open(helper.nrml("day2.txt")) as f:
    lines = f.read()

score = 0
rock = "AX"
paper = "BY"
scissors = "CZ"
for line in lines.split("\n"):
    l2, l1 = line.split(" ")

    if l1 in rock:
        score += 1
    elif l1 in paper:
        score += 2
    elif l1 in scissors:
        score += 3
    if (l1 in rock and l2 in scissors) or (l1 in paper and l2 in rock) or (l1 in scissors and l2 in paper):
        
        score += 6
    elif (l1 in paper and l2 in paper) or (l1 in scissors and l2 in scissors) or (l1 in rock and l2 in rock):
        score += 3

print(score)