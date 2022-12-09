dataStream = []


def parse_data():
    global dataStream
    # opening the file in read mode
    my_file = open("data.txt", "r")

    # reading the file
    data = my_file.read()

    # replacing end splitting the text
    # when newline ('\n') is seen.
    dataStream = data.split("\n")
    my_file.close()


def star_1():
    T = [0, 0]
    H = [0, 0]
    t_history = [T.copy()]
    for d in dataStream:
        ins = d.split(" ")
        if ins[0] == "R":
            H[1] += int(ins[1])
        elif ins[0] == "L":
            H[1] -= int(ins[1])
        elif ins[0] == "U":
            H[0] -= int(ins[1])
        elif ins[0] == "D":
            H[0] += int(ins[1])

        while abs(T[0] - H[0]) > 1 or abs(T[1] - H[1]) > 1:
            if T[0] < H[0]:
                T[0] += 1
            if T[0] > H[0]:
                T[0] -= 1
            if T[1] < H[1]:
                T[1] += 1
            if T[1] > H[1]:
                T[1] -= 1

            if T not in t_history: t_history.append(T.copy())
        print(H)
    print(len(t_history))

def star_2():
    T = [0, 0]
    H = [0, 0]
    tails = []
    tails.append(H)
    for i in range(9):
        tails.append(T.copy())

    t_history = [T.copy()]

    for d in dataStream:
        if d != "":
            ins = d.split(" ")
            moves = int(ins[1])
            while moves >= 1:
                if ins[0] == "R":
                    tails[0][1] += 1
                elif ins[0] == "L":
                    tails[0][1] -= 1
                elif ins[0] == "U":
                    tails[0][0] -= 1
                elif ins[0] == "D":
                    tails[0][0] += 1

                moves -= 1

                for i in range(1, len(tails)):
                    if abs(tails[i][0] - tails[i - 1][0]) > 1 or abs(tails[i][1] - tails[i - 1][1]) > 1:
                        if tails[i][0] < tails[i - 1][0]:
                            tails[i][0] += 1
                        if tails[i][0] > tails[i - 1][0]:
                            tails[i][0] -= 1
                        if tails[i][1] < tails[i - 1][1]:
                            tails[i][1] += 1
                        if tails[i][1] > tails[i - 1][1]:
                            tails[i][1] -= 1

                        if i == 9:
                            if tails[i] not in t_history: t_history.append(tails[i].copy())
        print(H)
    print(t_history)
    print(len(t_history))

parse_data()
print(dataStream)
star_2()


