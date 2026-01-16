class FileManager:
    def __init__(self, filename):
        self.file = open(filename, "w")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager("test.txt") as f:
    f.write("Using context manager")
