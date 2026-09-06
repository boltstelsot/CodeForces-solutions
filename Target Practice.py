for t in range(int(input())):
    pts = 0
    def checkingpt(i,j):
        global pts
        if i == 1 or i == 10 or j == 1 or j == 10:
            pts += 1
        elif (i == 2 or i == 9) or (j == 2 or j == 9):
            pts += 2
        elif (i == 3 or i == 8) or (j == 3 or j == 8):
            pts += 3
        elif (i == 4 or i == 7) or (j == 4 or j == 7):
            pts += 4
        elif (i == 5 or i == 6) or (j == 6 or j == 5):
            pts += 5
    for y in range(10):
        l = input()
        for x in range(10):
            if l[x] == "X":
                checkingpt((x+1),(y+1))
    print(pts)

#The CP-31 solution makes me feel wierd