class FileManager:
    def __init__(self, filename):
        self.file = open(filename, "w")

    def __enter__(self):
        return self.file
