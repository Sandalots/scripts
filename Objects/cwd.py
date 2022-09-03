import os
# Get current path

class Cwd:
    def __init__(self, path):
        self.cwd = os.getcwd()

if __name__ == '__main__':
    getcwd = Cwd(os.getcwd())
    print(getcwd.cwd)