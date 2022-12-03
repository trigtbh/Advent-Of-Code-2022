import helper
with open(helper.nrml("day2.txt")) as f:
    lines = f.read()

score = 0
rock = "AX"
paper = "BY"
scissors = "CZ"
for line in lines.split("\n"):
    turn, cond = line.split(" ")
    if cond == "Y":
        score += 3
        if turn in rock:
            score += 1
        elif turn in paper:
            score += 2
        elif turn in scissors:
            score += 3
    elif cond == "X":
        if turn in rock:
            score += 3
        elif turn in paper:
            score += 1
        elif turn in scissors:
            score += 2
    elif cond == "Z":
        score += 6
        if turn in rock:
            score += 2
        elif turn in paper:
            score += 3
        elif turn in scissors:
            score += 1
    
    
    


print(score)