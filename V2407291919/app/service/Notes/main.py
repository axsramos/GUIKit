import os
import sys


class ProgramNotes:
    def __init__(self, args=[]) -> None:
        if len(args) >= 2:
            if args[1] == 'start':
                self.start()

    def start(self):
        os.system("notepad.exe")


if __name__ == "__main__":
    ProgramNotes(sys.argv)
