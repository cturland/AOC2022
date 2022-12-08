dataStream = []
root = None


def parse_data():
    global dataStream
    # opening the file in read mode
    my_file = open("data.txt", "r")

    # reading the file
    data = my_file.read()

    # replacing end splitting the text
    # when newline ('\n') is seen.
    row = []
    for d in data:
        d = d.strip("\n")
        if d != "":
            row.append(int(d))
        else:
            dataStream.append(row)
            row=[]
    my_file.close()

def check_sight(row, col):
    # Check to left
    left = col - 1
    right = col + 1
    top = row - 1
    bottom = row + 1
    left_block = False
    right_block = False
    top_block = False
    bottom_block = False
    while left >= 0 or right <= len(dataStream[row]) - 1 or top >= 0 or bottom <= len(dataStream) - 1:
        if left >= 0 and dataStream[row][col] <= dataStream[row][left]:
            left_block = True
            left = -1
        else:
            left -= 1

        if right <= len(dataStream[row]) - 1 and dataStream[row][col] <= dataStream[row][right]:
            right_block = True
            right = len(dataStream)
        else:
            right += 1

        if top >= 0 and dataStream[row][col] <= dataStream[top][col]:
            top_block = True
            top = -1
        else:
            top -= 1

        if bottom <= len(dataStream) - 1 and dataStream[row][col] <= dataStream[bottom][col]:
            bottom_block = True
            bottom = len(dataStream)
        else:
            bottom += 1

    print(dataStream[row][col], left_block, right_block, top_block, bottom_block)
    if left_block and right_block and top_block and bottom_block:
        return 0
    else:
        return 1

def scenic_score(row, col):
    left = col - 1
    right = col + 1
    top = row - 1
    bottom = row + 1
    left_block = False
    right_block = False
    top_block = False
    bottom_block = False
    lscore = 0
    rscore = 0
    tscore = 0
    bscore = 0
    while left >= 0 or right <= len(dataStream[row]) - 1 or top >= 0 or bottom <= len(dataStream) - 1:
        if left >= 0 and dataStream[row][col] <= dataStream[row][left]:
            left_block = True
            left = -1
            lscore += 1
        elif left >= 0:
            left -= 1
            lscore += 1

        if right <= len(dataStream[row]) - 1 and dataStream[row][col] <= dataStream[row][right]:
            right_block = True
            right = len(dataStream)
            rscore += 1
        elif right <= len(dataStream[row]) - 1:
            right += 1
            rscore += 1

        if top >= 0 and dataStream[row][col] <= dataStream[top][col]:
            top_block = True
            top = -1
            tscore += 1
        elif top >= 0:
            top -= 1
            tscore += 1

        if bottom <= len(dataStream) - 1 and dataStream[row][col] <= dataStream[bottom][col]:
            bottom_block = True
            bottom = len(dataStream)
            bscore += 1
        elif bottom <= len(dataStream) - 1:
            bottom += 1
            bscore += 1

    #print(lscore, rscore, tscore, bscore)
    return lscore * rscore * tscore * bscore

def star_1():
    # -4 to not count corners twice
    total = (len(dataStream[0] * 2) + len(dataStream) * 2) - 4
    for row in range(1, len(dataStream) - 1):
        for col in range(1, len(dataStream[0]) - 1):
            total += check_sight(row, col)
    print(total)

def star_2():
    best = 0
    for row in range(1, len(dataStream) - 1):
        for col in range(1, len(dataStream[0]) - 1):
            score = scenic_score(row, col)
            if score > best:
                print(row, col, score)
                best = score
    print(best)


parse_data()
star_2()
