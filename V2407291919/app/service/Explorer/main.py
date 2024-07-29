import os
import sys


class ProgramExplorer:
    def __init__(self, args=[]) -> None:
        if len(args) >= 2:
            if args[1] == 'start':
                self.start()

    def start(self):
        os.system("explorer.exe")


if __name__ == "__main__":
    ProgramExplorer(sys.argv)
