# -*- coding: utf-8 -*-
from class_xo import xo

if __name__ == "__main__":
    print("+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+")
    print("START [x].\nEnter digit [ 1 - 9 ] or to stop [ stop ]!")
    while True:
        DIGIT = input(">>>>>>>>>>>>> ")
        if (DIGIT == "stop"): break
        if (DIGIT.isdigit()):
            if (1 <= int(DIGIT) <= 9):
                app = xo(DIGIT).out_in_console()
            else:
                print("Enter digit between 1 and 9!")
        else:
            print("Entered not a digit.")
    input("Press <Enter>...")
