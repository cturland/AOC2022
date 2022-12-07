from d7_file import File


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent

    def addFile(self, name, size):
        f = File(name, size)
        self.files.append(f)

    def addDir(self, name, parent):
        d = Directory(name, parent)
        self.directories.append(d)

    def dir_size(self):
        size = 0
        count = 0
        for f in self.files:
            size += f.size
        for d in self.directories:
            s, c = d.dir_size()
            size += s
            count += c
        if size < 100000:
            count += size
        return size, count

    def find_space(self, freeup):
        size = 0
        for f in self.files:
            size += f.size
        for d in self.directories:
            size += d.find_space(freeup)

        if size > freeup:
            print(self.name, size)

        return size

