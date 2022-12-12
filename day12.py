from warnings import warn
import heapq

class Node:
   pass

dataStream = []
start = 0
end = 0


def parse_data():
    global dataStream, start, end
    # opening the file in read mode
    my_file = open("test.txt", "r")

    # reading the file
    data = my_file.read()

    # replacing end splitting the text
    # when newline ('\n') is seen.
    dataStream = data.split("\n")
    for i, data in enumerate(dataStream):
        dataStream[i] = list(data)
        for j, letter in enumerate(dataStream[i]):
            if dataStream[i][j] not in ["S", "E"]:
                # dataStream[i][j] = (dataStream[i][j], ord(dataStream[i][j]))
                dataStream[i][j] = ord(dataStream[i][j]) - 64
            elif dataStream[i][j] == "S":
                # dataStream[i][j] = (dataStream[i][j], 0)
                dataStream[i][j] = 0
                start = (i, j)
            elif dataStream[i][j] == "E":
                # dataStream[i][j] = (dataStream[i][j], 0)
                dataStream[i][j] = 0
                end = (i, j)
    # Remove the end empty line
    dataStream.pop(len(dataStream) - 1)
    my_file.close()

def return_path(current_node):
    pass


def astar(maze, start, end):
    pass


def star_1():

    path = astar(dataStream, start, end)
    print(path)

parse_data()
print(dataStream)
star_1()
