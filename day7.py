from d7_dir import Directory

dataStream = None
root = None


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

def setup_tree():
    global root

    root = Directory("/", None)
    current = root
    # Remove first instruction as it is always "$ CD /"
    dataStream.pop(0)

    for line in dataStream:
        # Move to a new directory
        ins = line.split(" ")
        if ins[0] == "$":
            if ins[1] == "cd" and ins[2] != "..":
                # Need to deal with moving back CD ..
                for d in current.directories:
                    if d.name == ins[2]:
                        current = d
                        break
            elif ins[1] == "cd" and ins[2] == "..":
                current = current.parent
        elif ins[0] == "dir":
            current.addDir(ins[1], current)
        elif len(ins) > 1:
            current.addFile(ins[1], ins[0])


def star_1():
    print(root.dir_size())


def star_2():
    available = 70000000
    needed = 30000000
    total, z = root.dir_size()
    used = available - total
    print(used, "current space available")
    freeup = needed - used
    print("Need to free up", freeup)
    root.find_space(freeup)


parse_data()
setup_tree()
star_2()






