import os
import sys


class ProgramCalculator:
    def __init__(self, args=[]) -> None:
        if len(args) >= 2:
            if args[1] == 'start':
                self.start()

    def start(self):
        os.system("calc.exe")


if __name__ == "__main__":
    ProgramCalculator(sys.argv)
