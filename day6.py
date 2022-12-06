dataStream = None


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
    for line in dataStream:

        for i in range(0, len(line) - 4, 1):
            repeats = []
            copies = False
            for j in range(i, i + 4):
                if line[j] not in repeats:
                    repeats.append(line[j])
                else:
                    copies = True
                    break
            if not copies:
                print(i + 4)
                break

def star_2():
    for line in dataStream:

        for i in range(0, len(line) - 14, 1):
            repeats = []
            copies = False
            for j in range(i, i + 14):
                if line[j] not in repeats:
                    repeats.append(line[j])
                else:
                    copies = True
                    break
            if not copies:
                print(i + 14)
                break


parse_data()
star_2()
