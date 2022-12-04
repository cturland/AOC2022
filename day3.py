import collections

# opening the file in read mode
my_file = open("data.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data = data.split("\n")
my_file.close()

# Day 3 star 1 solution
def star_1():
    duplicates = []
    for line in data:
        c1 = line[0:len(line) // 2]
        c2 = line[len(line) // 2:]

        found = False
        for i in range(len(c1)):
            for j in range(len(c2)):
                if c1[i] == c2[j]:
                    if ord(c1[i]) > 97:
                        value = ord(c1[i]) - 96
                    else:
                        value = ord(c1[i]) - 38 # + 26 for lower case
                    duplicates.append(value)
                    found = True
                    break
            if found: break
    print(sum(duplicates))


# Star 2 solution
def star_2():
    duplicates = []
    count = 0
    group = []
    for line in data:
        count += 1
        group.append(line)
        if count == 3:
            same = list(set(group[0]).intersection(group[1], group[2]))
            if ord(same[0]) > 97:
                value = ord(same[0]) - 96
            else:
                value = ord(same[0]) - 38  # + 26 for lower case
            duplicates.append(value)
            group = []
            count = 0
    print(sum(duplicates))

star_2()
