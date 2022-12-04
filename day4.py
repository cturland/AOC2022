# opening the file in read mode
my_file = open("data.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data = data.split("\n")
my_file.close()


def star_1():
    count = 0
    for line in data:
        pairs = line.split(",")
        sections = []
        for elf in pairs:
            limits = elf.split("-")
            indv = []
            for i in range(int(limits[0]), int(limits[1]) + 1):
                indv.append(i)
            sections.append(indv)
        #print(sections)
        same = list(set(sections[0]).intersection(sections[1]))

        if len(same) == len(sections[0]) or len(same) == len(sections[1]):
            count += 1
        sections = []
    print(count)


def star_2():
    count = 0
    for line in data:
        pairs = line.split(",")
        sections = []
        for elf in pairs:
            limits = elf.split("-")
            indv = []
            for i in range(int(limits[0]), int(limits[1]) + 1):
                indv.append(i)
            sections.append(indv)
        # print(sections)
        same = list(set(sections[0]).intersection(sections[1]))

        if len(same) > 0:
            count += 1
        sections = []
    print(count)


star_2()