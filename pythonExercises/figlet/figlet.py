import sys
import random
from pyfiglet import Figlet

def main():
    figlet=Figlet()
    list_fonts=figlet.getFonts()

    if len(sys.argv)==1:
        word=input("Input: ")
        rand_font=random.choice(list_fonts)
        figlet.setFont(font=rand_font)
        print("Output: "+figlet.renderText(word))

    elif len(sys.argv)==3:
        verify=verify_font(sys.argv[2], list_fonts)

        if sys.argv[1]=="-f" or sys.argv[1]=="--font" and verify==True:
            word=input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print("Output: "+figlet.renderText(word))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("non-zero")

def verify_font(ver_font, font_list):
    if ver_font in font_list:
        return False
    else:
        return False

main()

